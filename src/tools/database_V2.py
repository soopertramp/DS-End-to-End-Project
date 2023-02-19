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

# Set database to True
database = True

# If database is True, create a new database with the given database name 
# using the connect_to_mysql() and create_database() functions 
if database:
    mydb, cursor = connect_to_mysql(host, user, password)
    create_database(cursor, database_name)
# If database is False, create a new table with the given table name and column type
# and insert the data from the dataframe
else:
    create_table(database_name, table_name, col_type, cursor)
    df = get_data(data)
    # create the schema for the database using the create_db_schema() function 
    col_type, values = create_db_schema(df)
    for i,row in df.iterrows():
        # create an SQL query string for each row using the values list and the table name
        # and execute it using the cursor object 
        sql = f"INSERT INTO {table_name} VALUES ({values})"
        cursor.execute(sql, tuple(row))
        # commit the changes to the database
        mydb.commit()
    # print the number of records inserted
    print(cursor.rowcount, "Record inserted")