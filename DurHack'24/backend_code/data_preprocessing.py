# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def data_processing(data):
    # Convert MongoDB collection to DataFrame for EDA

    transactions = data['statement_description']
    base_data = {key: data[key] for key in data if key != 'statement_description'}

    # Create a DataFrame for the transactions
    df = pd.DataFrame(transactions)

    # Add base customer data to each row of the transactions DataFrame
    for key, value in base_data.items():
        df[key] = value

    # Rearrange columns to match the specified order
    final_columns = [
        "id", "customer_name", "customer_id", "account_type",
        "statement_date", "current_balance", "opening_balance",
        "account_no", "email", "phoneNo",
        "transaction_date", "transaction_amount",
        "transaction_decription", "transaction_id", "transaction_type"
    ]
    df = df[final_columns]

# Display the DataFrame
    #print(df)
    eda_summary = {
            "data_shape": df.shape,
            "columns": df.columns.tolist(),
            "head": df.head().to_dict(orient='records'),
            "description": df.describe(include='all').to_dict(),
            "transaction_type_counts": df['transaction_type'].value_counts().to_dict()
        }

        # Visualizations
    plt.switch_backend('Agg')
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='transaction_type')
    plt.title('Transaction Type Distribution')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.savefig('static/transaction_type_distribution.png')  # Save the plot
    plt.close()

    return [eda_summary,df] 