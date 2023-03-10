#import necessary libraries 
import matplotlib.pyplot as plt
import pandas as pd

#reading the data
df = pd.read_csv('data/supermarket_sales.csv')

# convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

#sorting the data by date in ascending order
df.sort_values(by='date', ascending=True, ignore_index=True, inplace = True)

#splitting tables
table1 = df[['invoice_id', 'branch', 'city', 'customer_type','gender','product_line', 'unit_price']]

table2 = df[['invoice_id', 'quantity', 'tax_5_percent', 'total', 'date', 'time', 'payment']]

table3 = df[['invoice_id', 'cogs', 'gross_margin_percentage', 'gross_income', 'rating',]]

# Save the tables as CSV files
table1.to_csv('table1.csv', index=False)
table2.to_csv('table2.csv', index=False)
table3.to_csv('table3.csv', index=False)