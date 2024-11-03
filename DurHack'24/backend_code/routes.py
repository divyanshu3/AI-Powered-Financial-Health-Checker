from flask import Flask, request, jsonify
from flask_api import status
from models import save_in_database,find,getAll
from bson.objectid import ObjectId  # Import ObjectId
import re
from data_preprocessing import data_processing
app = Flask(__name__)

# Define the required fields and their constraints
REQUIRED_FIELDS = [
    "id", "customer_name", "customer_id", "account_type",
    "statement_date", "current_balance", "opening_balance",
    "account_no", "email", "phoneNo", "statement_description"
]

ACCOUNT_TYPES = {"savings", "current"}
TRANSACTION_TYPES = {"debit", "credit"}

# Helper function to validate the JSON input
def validate_input(data):
    missing_fields = []
    invalid_fields = {}

    # Validate top-level fields
    for field in REQUIRED_FIELDS:
        if field not in data or data[field] in [None, '', []]:
            missing_fields.append(field)

    # Specific checks
    if "account_type" in data and data["account_type"] not in ACCOUNT_TYPES:
        invalid_fields["account_type"] = "Must be 'savings' or 'current'."

    if "email" in data and not re.match(r"[^@]+@[^@]+\.[^@]+", data["email"]):
        invalid_fields["email"] = "Invalid email format."

    if "phoneNo" in data and (not data["phoneNo"].isdigit() or len(data["phoneNo"]) != 10):
        invalid_fields["phoneNo"] = "Must be a 10-digit phone number."

    # Check the nested statement_description for required fields
    if "statement_description" in data:
        for transaction in data["statement_description"]:
            for field in ["transaction_date", "transaction_amount", "transaction_decription", "transaction_id", "transaction_type"]:
                if field not in transaction or transaction[field] in [None, '']:
                    missing_fields.append(field)
            if "transaction_type" in transaction and transaction["transaction_type"] not in TRANSACTION_TYPES:
                invalid_fields.setdefault("transaction_type", []).append(transaction["transaction_type"])

    return missing_fields, invalid_fields

@app.route('/v1/financialreport', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        
        # Validate input
        missing_fields, invalid_fields = validate_input(data)
        if missing_fields or invalid_fields:
            return jsonify({
                "status": "failure",
                "description": "Incorrect request received. Parsing failed.",
                "missing_fields": missing_fields,
                "invalid_fields": invalid_fields
            }), status.HTTP_400_BAD_REQUEST
        
        processed_data = data_processing(data)
        
        # Save the valid data in MongoDB
        result = save_in_database(processed_data[1].to_dict("records"))
        print(processed_data[1])
        saved_data = [] 
        for k in find(data["id"]):
            saved_data.append(serialize_doc(k))

        # Process the valid data here (e.g., store in database)
        return jsonify({
            "status": "success",
            "data": saved_data,
            "eda_summary": processed_data[0]
        }), status.HTTP_200_OK
    
    except Exception as e:
        return jsonify({
            "status": "failure",
            "description": f"An error occurred: {str(e)}"
        }), status.HTTP_500_INTERNAL_SERVER_ERROR

# Function to serialize MongoDB documents
def serialize_doc(doc):
    doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
    return doc