# Import necessary libraries
import pandas as pd
import sqlite3

# Read customer data from CSV file
customers_df = pd.read_csv('customer.csv')  # Load customer information from 'customer.csv'

# Read order data from CSV file
orders_df = pd.read_csv('orders.csv')       # Load order information from 'orders.csv'

# Merge the customer and order data based on 'CustomerID'
merged_df = pd.merge(orders_df, customers_df, on='CustomerID', how='inner')  # Combine order and customer data

# Calculate the total amount for each order
merged_df['TotalAmount'] = merged_df['Quantity'] * merged_df['Price']  # Compute TotalAmount as Quantity * Price

# Add a 'Status' column to indicate whether the order is 'New' or 'Old'
merged_df['Status'] = merged_df['OrderDate'].apply(lambda d: 'New' if d.startswith('2025-03') else 'Old')  # Define order status based on date

# Filter high-value orders (TotalAmount > 5000)
high_value_orders = merged_df[merged_df['TotalAmount'] > 5000]  # Select orders with TotalAmount greater than 5000

# Connect to SQLite database
conn = sqlite3.connect('ecommerce.db')  # Establish a connection to the SQLite database

# Create a table to store high-value orders if it doesn't already exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS HighValueOrders (
    OrderID INTEGER,
    CustomerID INTEGER,
    Name TEXT,
    Email TEXT,
    Product TEXT,
    Quantity INTEGER,
    Price REAL,
    OrderDate TEXT,
    TotalAmount REAL,
    Status TEXT
)
'''
conn.execute(create_table_query)  # Execute the SQL query to create the table

# Load the high-value orders into the SQLite database
high_value_orders.to_sql('HighValueOrders', conn, if_exists='replace', index=False)  # Insert data into the table

# Query and print the high-value orders from the database
result = conn.execute('SELECT * FROM HighValueOrders')  # Retrieve data from the table
for row in result.fetchall():  # Fetch and print each row
    print(row)

# Close the database connection
conn.close()

# Print a success message
print("ETL process completed successfully!")