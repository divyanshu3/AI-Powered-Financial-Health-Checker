import pandas as pd

# Your JSON data
data = [
    {
        "id": "1011011_Nov_2024",
        "customer_name": "John Doe",
        "customer_id": "10001",
        "account_type": "savings",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "1500.50",
        "opening_balance": "1000.00",
        "account_no": "acc001",
        "email": "johndoe@example.com",
        "phoneNo": "1234567890",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T09:00:00",
                "transaction_amount": "200.00",
                "transaction_decription": "grocery shopping",
                "transaction_id": "trans001",
                "transaction_type": ""
            },
            {
                "transaction_date": "02-11-2024T10:00:00",
                "transaction_amount": "500.00",
                "transaction_decription": "salary credited",
                "transaction_id": "trans002",
                "transaction_type": "credit"
            }
        ]
    },
    {
        "id": "1021021_Nov_2024",
        "customer_name": "Alice Smith",
        "customer_id": "10002",
        "account_type": "current",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "2800.75",
        "opening_balance": "2500.00",
        "account_no": "acc002",
        "email": "alicesmith@example.com",
        "phoneNo": "2345678901",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T12:00:00",
                "transaction_amount": "1500.00",
                "transaction_decription": "paid rent",
                "transaction_id": "trans003",
                "transaction_type": "debit"
            },
            {
                "transaction_date": "02-11-2024T15:00:00",
                "transaction_amount": "300.00",
                "transaction_decription": "utility bill payment",
                "transaction_id": "trans004",
                "transaction_type": "debit"
            }
        ]
    },
    {
        "id": "1031031_Nov_2024",
        "customer_name": "Bob Johnson",
        "customer_id": "10003",
        "account_type": "savings",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "3600.00",
        "opening_balance": "3300.00",
        "account_no": "acc003",
        "email": "bobjohnson@example.com",
        "phoneNo": "3456789012",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T14:00:00",
                "transaction_amount": "600.00",
                "transaction_decription": "car loan payment",
                "transaction_id": "trans005",
                "transaction_type": "debit"
            },
            {
                "transaction_date": "02-11-2024T11:00:00",
                "transaction_amount": "900.00",
                "transaction_decription": "credit card payment",
                "transaction_id": "trans006",
                "transaction_type": "debit"
            }
        ]
    },
    {
        "id": "1041041_Nov_2024",
        "customer_name": "Carol White",
        "customer_id": "10004",
        "account_type": "current",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "2200.00",
        "opening_balance": "2000.00",
        "account_no": "acc004",
        "email": "carolwhite@example.com",
        "phoneNo": "4567890123",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T16:00:00",
                "transaction_amount": "400.00",
                "transaction_decription": "restaurant dining",
                "transaction_id": "trans007",
                "transaction_type": "debit"
            },
            {
                "transaction_date": "02-11-2024T18:00:00",
                "transaction_amount": "700.00",
                "transaction_decription": "investment in stocks",
                "transaction_id": "trans008",
                "transaction_type": "credit"
            }
        ]
    },
    {
        "id": "1051051_Nov_2024",
        "customer_name": "David Brown",
        "customer_id": "10005",
        "account_type": "savings",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "4000.00",
        "opening_balance": "3700.00",
        "account_no": "acc005",
        "email": "davidbrown@example.com",
        "phoneNo": "5678901234",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T08:00:00",
                "transaction_amount": "800.00",
                "transaction_decription": "health insurance payment",
                "transaction_id": "trans009",
                "transaction_type": "debit"
            },
            {
                "transaction_date": "02-11-2024T10:00:00",
                "transaction_amount": "500.00",
                "transaction_decription": "savings deposit",
                "transaction_id": "trans010",
                "transaction_type": "credit"
            }
        ]
    },
    {
        "id": "1061061_Nov_2024",
        "customer_name": "Emma Green",
        "customer_id": "10006",
        "account_type": "current",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "2900.50",
        "opening_balance": "2600.00",
        "account_no": "acc006",
        "email": "emmagreen@example.com",
        "phoneNo": "6789012345",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T14:00:00",
                "transaction_amount": "300.00",
                "transaction_decription": "internet bill payment",
                "transaction_id": "trans011",
                "transaction_type": "debit"
            },
            {
                "transaction_date": "02-11-2024T09:00:00",
                "transaction_amount": "600.00",
                "transaction_decription": "bonus credited",
                "transaction_id": "trans012",
                "transaction_type": "credit"
            }
        ]
    },
    {
        "id": "1071071_Nov_2024",
        "customer_name": "Frank Harris",
        "customer_id": "10007",
        "account_type": "savings",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "3200.25",
        "opening_balance": "3000.00",
        "account_no": "acc007",
        "email": "frankharris@example.com",
        "phoneNo": "7890123456",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T11:00:00",
                "transaction_amount": "250.00",
                "transaction_decription": "gym membership fee",
                "transaction_id": "trans013",
                "transaction_type": "debit"
            },
            {
                "transaction_date": "02-11-2024T13:00:00",
                "transaction_amount": "500.00",
                "transaction_decription": "gift received",
                "transaction_id": "trans014",
                "transaction_type": "credit"
            }
        ]
    },
    {
        "id": "1081081_Nov_2024",
        "customer_name": "Grace Lee",
        "customer_id": "10008",
        "account_type": "current",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "2500.80",
        "opening_balance": "2300.00",
        "account_no": "acc008",
        "email": "gracelee@example.com",
        "phoneNo": "8901234567",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T12:00:00",
                "transaction_amount": "200.00",
                "transaction_decription": "mobile bill payment",
                "transaction_id": "trans015",
                "transaction_type": "debit"
            },
            {
                "transaction_date": "02-11-2024T19:00:00",
                "transaction_amount": "300.00",
                "transaction_decription": "received refund",
                "transaction_id": "trans016",
                "transaction_type": "credit"
            }
        ]
    },
    {
        "id": "1091091_Nov_2024",
        "customer_name": "Henry King",
        "customer_id": "10009",
        "account_type": "savings",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "4200.40",
        "opening_balance": "3900.00",
        "account_no": "acc009",
        "email": "henryking@example.com",
        "phoneNo": "9012345678",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T17:00:00",
                "transaction_amount": "700.00",
                "transaction_decription": "furniture purchase",
                "transaction_id": "trans017",
                "transaction_type": "debit"
            },
            {
                "transaction_date": "02-11-2024T20:00:00",
                "transaction_amount": "1000.00",
                "transaction_decription": "salary credited",
                "transaction_id": "trans018",
                "transaction_type": "credit"
            }
        ]
    },
    {
        "id": "1101101_Nov_2024",
        "customer_name": "Ivy Miller",
        "customer_id": "10010",
        "account_type": "current",
        "statement_date": "03-11-2024T20:00:00",
        "current_balance": "3100.00",
        "opening_balance": "2900.00",
        "account_no": "acc010",
        "email": "ivymiller@example.com",
        "phoneNo": "0123456789",
        "statement_description": [
            {
                "transaction_date": "01-11-2024T13:00:00",
                "transaction_amount": "400.00",
                "transaction_decription": "clothing purchase",
                "transaction_id": "trans019",
                "transaction_type": "debit"
            },
            {
                "transaction_date": "02-11-2024T17:00:00",
                "transaction_amount": "700.00",
                "transaction_decription": "received payment for services",
                "transaction_id": "trans020",
                "transaction_type": "credit"
            }
        ]
    },
    {
    "id": "1111111_Nov_2024",
    "customer_name": "John Doe",
    "customer_id": "10001",
    "account_type": "savings",
    "statement_date": "03-11-2024T20:00:00",
    "current_balance": "4200.50",
    "opening_balance": "4000.00",
    "account_no": "acc001",
    "email": "johndoe@example.com",
    "phoneNo": "1234567890",
    "statement_description": [
        {
            "transaction_date": "01-11-2024T09:00:00",
            "transaction_amount": "500.00",
            "transaction_decription": "salary credited",
            "transaction_id": "trans001",
            "transaction_type": "credit"
        },
        {
            "transaction_date": "01-11-2024T10:30:00",
            "transaction_amount": "150.00",
            "transaction_decription": "grocery shopping",
            "transaction_id": "trans002",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "01-11-2024T13:00:00",
            "transaction_amount": "200.00",
            "transaction_decription": "paid electricity bill",
            "transaction_id": "trans003",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "02-11-2024T11:00:00",
            "transaction_amount": "350.00",
            "transaction_decription": "insurance premium payment",
            "transaction_id": "trans004",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "02-11-2024T15:30:00",
            "transaction_amount": "1200.00",
            "transaction_decription": "received tax refund",
            "transaction_id": "trans005",
            "transaction_type": "credit"
        },
        {
            "transaction_date": "03-11-2024T08:00:00",
            "transaction_amount": "100.00",
            "transaction_decription": "gym membership fee",
            "transaction_id": "trans006",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "03-11-2024T09:00:00",
            "transaction_amount": "200.00",
            "transaction_decription": "donation to charity",
            "transaction_id": "trans007",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "03-11-2024T11:00:00",
            "transaction_amount": "50.00",
            "transaction_decription": "movie tickets purchase",
            "transaction_id": "trans008",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "03-11-2024T12:00:00",
            "transaction_amount": "300.00",
            "transaction_decription": "received payment for freelance work",
            "transaction_id": "trans009",
            "transaction_type": "credit"
        },
        {
            "transaction_date": "03-11-2024T14:00:00",
            "transaction_amount": "80.00",
            "transaction_decription": "fuel for car",
            "transaction_id": "trans010",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "03-11-2024T16:00:00",
            "transaction_amount": "600.00",
            "transaction_decription": "home repair services",
            "transaction_id": "trans011",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "04-11-2024T09:30:00",
            "transaction_amount": "500.00",
            "transaction_decription": "bonus received",
            "transaction_id": "trans012",
            "transaction_type": "credit"
        },
        {
            "transaction_date": "04-11-2024T10:00:00",
            "transaction_amount": "75.00",
            "transaction_decription": "coffee shop",
            "transaction_id": "trans013",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "04-11-2024T11:30:00",
            "transaction_amount": "400.00",
            "transaction_decription": "paid for online course",
            "transaction_id": "trans014",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "05-11-2024T14:00:00",
            "transaction_amount": "900.00",
            "transaction_decription": "salary credited",
            "transaction_id": "trans015",
            "transaction_type": "credit"
        },
        {
            "transaction_date": "05-11-2024T15:00:00",
            "transaction_amount": "300.00",
            "transaction_decription": "gifts for family",
            "transaction_id": "trans016",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "05-11-2024T16:30:00",
            "transaction_amount": "250.00",
            "transaction_decription": "paid for concert tickets",
            "transaction_id": "trans017",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "06-11-2024T10:00:00",
            "transaction_amount": "200.00",
            "transaction_decription": "received bonus from side gig",
            "transaction_id": "trans018",
            "transaction_type": "credit"
        },
        {
            "transaction_date": "06-11-2024T11:00:00",
            "transaction_amount": "600.00",
            "transaction_decription": "purchase of new laptop",
            "transaction_id": "trans019",
            "transaction_type": "debit"
        },
        {
            "transaction_date": "06-11-2024T12:30:00",
            "transaction_amount": "150.00",
            "transaction_decription": "monthly subscription service",
            "transaction_id": "trans020",
            "transaction_type": "debit"
        }
    ]
}

]

# Prepare an empty list to collect rows
rows = []

# Loop through each customer record
for record in data:
    customer_info = {
        "id": record["id"],
        "customer_name": record["customer_name"],
        "customer_id": record["customer_id"],
        "account_type": record["account_type"],
        "statement_date": record["statement_date"],
        "current_balance": record["current_balance"],
        "opening_balance": record["opening_balance"],
        "account_no": record["account_no"],
        "email": record["email"],
        "phoneNo": record["phoneNo"],
    }

    # Loop through each transaction
    for transaction in record["statement_description"]:
        row = {**customer_info, **transaction}
        rows.append(row)

# Create a DataFrame from the collected rows
df = pd.DataFrame(rows)

# Rearrange columns to match the specified order
final_columns = [
    "id", "customer_name", "customer_id", "account_type",
    "statement_date", "current_balance", "opening_balance",
    "account_no", "email", "phoneNo",
    "transaction_date", "transaction_amount",
    "transaction_decription", "transaction_id", "transaction_type"
]
df = df[final_columns]

# Create a CSV file
csv_file_path = 'customer_statements.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV file created: {csv_file_path}")
