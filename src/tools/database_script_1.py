import mysql.connector as mysql
from pathlib import Path 
import os
import pandas as pd
from dotenv import load_dotenv
import csv

#STEP 1: CONNECTION TO MYSQL

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="password"
)

print(mydb)

#STEP 2: CONNECTOR

""" Create a cursor object : A cursor is a temporary storage area in a 
database management system. You can use it to execute SQL statements 
and retrieve the results. """

cursor = mydb.cursor()

#STEP 3: SQL QUERY

drop_db_query = 'DROP DATABASE IF EXISTS supermarket'
cursor.execute(drop_db_query)

# show databases

cursor.execute('SHOW DATABASES')
databases = cursor.fetchall()
databases

for data in databases:
  print(data)
  
#create database  

create_db_query = 'CREATE DATABASE supermarket'
cursor.execute(create_db_query)

## show databases
cursor.execute('SHOW DATABASES')
databases = cursor.fetchall()
databases

#read the data using pandas ~ convert it to function 

df = pd.read_csv("data\supermarket_sales.csv")
df

#drop and create a new table

cursor.execute('USE supermarket')
cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
cursor.execute(f"CREATE TABLE {table_name} ({col_type})")
               
df.columns

#insert data into table

for i,row in df.iterrows():
  #here %S means string values 
  sql = f"INSERT INTO {table_name} (invoice_id, branch, city, customer_type, gender, product_line, unit_price, quantity, tax_5_percent, total, date, time, payment, cogs, gross_margin_percentage, gross_income, rating) VALUES ({values})"
  cursor.execute(sql, tuple(row))
  print("Record inserted")
  # the connection is not auto committed by default, so we must commit to save our changes
  mydb.commit()
  
# parameters

col_type, values = create_db_schema(df)
table_name = 'customers'