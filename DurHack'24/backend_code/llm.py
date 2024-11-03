import pandas as pd
import numpy as np
import openai  # Ensure you have the OpenAI library installed
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from models import getAll

# Set your OpenAI API key
openai.api_key = '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'
# Sample Data: Replace with your actual CSV data loading
data = getAll()

df = pd.DataFrame(list(data))
df = df.drop(columns=['_id'])
#df = df[df["customer_name"] == 'John Doe'] 


# Feature Engineeringccle
def create_features(df):
    features = df.groupby('customer_name').agg(
        total_credits=('transaction_amount', lambda x: x[df['transaction_type'] == 'credit'].sum()),
        total_debits=('transaction_amount', lambda x: x[df['transaction_type'] == 'debit'].sum()),
        transaction_count=('transaction_amount', 'count')
    ).reset_index()
    features['net_balance'] = pd.to_numeric(features['total_credits']) - pd.to_numeric(features['total_debits'])
    features['average_savings_per_transaction'] = pd.to_numeric(features['total_credits']) / (pd.to_numeric(features['transaction_count']) + 1e-5)
    
    return features

features = create_features(df)

# LLM Integration for Advice Generation
def generate_advice(customer_row):
    prompt = (
        f"Customer Name: {customer_row['customer_name']}\n"
        f"Net Balance: {customer_row['net_balance']}\n"
        f"Average Savings per Transaction: {customer_row['average_savings_per_transaction']}\n"
        f"Total Credits: {customer_row['total_credits']}\n"
        f"Total Debits: {customer_row['total_debits']}\n\n"
        "Based on the above information, provide personalized financial advice."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the model you prefer
        messages=[{"role": "user", "content": prompt}]
    )
    
    advice = response.choices[0].message['content'].strip()
    return advice

# Generate advice for each customer
#features['financial_advice'] = features.apply(generate_advice, axis=1)

# Output the results
print(features[['customer_name', 'net_balance', 'average_savings_per_transaction']])

# Split data into train and test sets for credit score prediction
# Simulate target values (replace with actual credit score data)
features['credit_score'] = np.random.randint(600, 800, size=len(features))

X = features[['total_credits', 'total_debits', 'transaction_count', 'net_balance', 'average_savings_per_transaction']]
y = features['credit_score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'R² Score: {r2}')
