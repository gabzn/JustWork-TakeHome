import pandas as pd
from Customer import Customer

def process_customers(df_transactions, customers, customer_ids):
    for id in customer_ids:
        # Get all transactions by a specific customer
        customer_transactions = df_transactions[df_transactions['customer_id'] == id][['date', 'amount']]
    
        # Sort his transactions by date and the amount because we want to apply credit transactions first
        customer_transactions.sort_values(['date', 'amount'], ascending=[True, False], inplace=True)
    
        # Create an instance of customer and append it to the customer list
        customers.append(Customer(id, customer_transactions))

def make_csv_output(customers):
    reports = []
    for customer in customers:
        reports.extend(customer.generate_report())
    pd.DataFrame(reports).to_csv('output.csv', header=False, index=False)

def main():
    df_transactions = pd.read_csv('input.csv', header=0, names=['customer_id', 'date', 'amount'])
    df_transactions.dropna(inplace=True)  

    # Change the value of date column to type datetime for sorting
    df_transactions['date'] = pd.to_datetime(df_transactions['date'])

    # Use customer_id to find all transactions belong to a customer 
    customers = []
    customer_ids = df_transactions['customer_id'].unique()
    
    process_customers(df_transactions, customers, customer_ids)
    make_csv_output(customers)

if __name__ == "__main__":
    main()