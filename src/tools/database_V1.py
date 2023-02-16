# import necessary libraries
import mysql.connector as mysql
from pathlib import Path 
import os
import pandas as pd
from dotenv import load_dotenv
import csv
from utils import connect_to_mysql, get_data, create_database, create_table, create_db_schema

# Step 1: Connect to MySQL server
# define host, user, password, and database name
host = 'localhost'
user = 'root'
password = 'password'
database_name = 'supermarket'

# call connect_to_mysql() function to establish connection
mydb, cursor = connect_to_mysql(host, user, password)

# Step 2: Create a new database
# call create_database() function to create a new database with the given name
create_database(cursor, database_name)

# Step 3: Read data from a CSV file using pandas
# load the CSV file into a dataframe using pandas
df = get_data("data\supermarket_sales.csv")
df

# Step 4: Create table schema
# call create_db_schema() function to create column names and types for the table schema
col_type, values = create_db_schema(df)

# Step 5: Create a new table
# call create_table() function to create a new table with the given schema in the database
create_table(database_name, 'customers', col_type, cursor)

# Step 6: Insert data into the table
# iterate over each row in the dataframe and insert it into the table using a for loop
for i,row in df.iterrows():
  # create an SQL query string for each row using the values list and the table name
  # and execute it using the cursor object 
  sql = f"INSERT INTO {table_name} VALUES ({values})"
  cursor.execute(sql, tuple(row))
  # commit the changes to the database
  mydb.commit()

# print the number of records inserted into the table  
print(cursor.rowcount, "Record inserted")