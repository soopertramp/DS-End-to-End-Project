# import necessary libraries
import csv
import os
from pathlib import Path

import mysql.connector as mysql
import pandas as pd
from dotenv import load_dotenv

from utils import (connect_to_mysql, create_database, create_db_schema,
                   create_table, get_data)

# define variables
host = 'localhost'
user = 'root'
password = 'password'
database_name = 'supermarket'
data = Path(os.path.join("data","supermarket_sales.csv"))
table_name = "customers"

# Step 1: Connect to MySQL server
# call connect_to_mysql() function to establish connection
mydb, cursor = connect_to_mysql(host, user, password)

# Step 2: Create a new database
# call create_database() function to create a new database with the given name
create_database(cursor, database_name)

# Step 3: Read data from a CSV file using pandas
# load the CSV file into a dataframe using pandas
df = get_data(data)

# Step 4: Create table schema
# call create_db_schema() function to create column names and types for the table schema
col_type, values = create_db_schema(df)

# Step 5: Create a new table
# call create_table() function to create a new table with the given schema in the database
create_table(database_name, table_name, col_type, cursor)

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