import mysql.connector as mysql
from pathlib import Path 
import os
import pandas as pd
from dotenv import load_dotenv

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="password"
)

print(mydb)

""" Create a cursor object : A cursor is a temporary storage area in a 
database management system. You can use it to execute SQL statements 
and retrieve the results. """

cursor = mydb.cursor()

drop_db_query = 'DROP DATABASE supermarket'
cursor.execute(drop_db_query)

create_db_query = 'CREATE DATABASE supermarket'
cursor.execute(create_db_query)

## show databases
cursor.execute('SHOW DATABASES')
record = cursor.fetchall()
record

cursor.execute('USE supermarket')
cursor.execute('DROP TABLE IF EXISTS ')

# ## drop and create new table
# cursor.execute('USE groceries')
# cursor.execute('DROP TABLE IF EXISTS sales;')
# cursor.execute('CREATE TABLE sales (id VARCHAR(255), timestamp VARCHAR(255), temperature DECIMAL(6,2))')

# ## insert data into table
# sql = "INSERT INTO sales (id, timestamp, temperature) VALUES (%s, %s, %s)"
# val = ("d1ca1ef8-0eac-42fc-af80-97106efc7b13", "2022-03-07 15:55:20", 2.96)
# cursor.execute(sql, val)
# conn.commit()
# print(cursor.rowcount, "record inserted.")

# def get_data(path: str) -> pd.DataFrame:
#     """_summary_

#     Args:
#         path (str): _description_

#     Returns:
#         pd.DataFrame: _description_
#     """
#     df = pd.read_csv(path)
#     df.drop(columns=['Unnamed: 0'], inplace=True, axis=1, errors='ignore')
#     return df # give me modified data back so that it can assigned to a variable

# def create_db_schema(data: pd.DataFrame) -> Tuple[str, str]:
#     types = []
#     for i in df.dtypes:
#         if i == 'object':
#             types.append('VARCHAR(255)')
#         elif i == 'float64':
#             types.append('DECIMAL(6,2)')
#     col_type = list(zip(df.columns.values, types))
#     col_type = tuple([" ".join(i) for i in col_type])
#     col_type = ", ".join(col_type)
#     values = ', '.join(['%s' for _ in range(len(df.columns))])
#     return col_type, values
# create_db_schema(df)