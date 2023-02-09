#importing the MySQL Connector library

import mysql.connector as mysql

# Establish a connection to the database

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="password"
)

print(mydb)

""" Create a cursor object : A cursor is a temporary storage area in a 
database management system. You can use it to execute SQL statements 
and retrieve the results. """

mycursor = mydb.cursor()

#Executing "SHOW DATABASES" shows the databases on your computer

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
  
#Create a database

mycursor.execute("CREATE DATABASE IF NOT EXISTS supermarket")

#Checking if that works

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
  
#use database

mycursor.execute("USE DATABASE supermarket")
  
# Create a table

mycursor.execute("CREATE TABLE supermarket_sales (invoice_id INT, branch CHAR, city VARCHAR, customer_type VARCHAR, gender VARCHAR, product_line VARCHAR, unit_price FLOAT, quantity INT, tax_5_percent FLOAT, total FLOAT, date DATE, time TIME, payment VARCHAR, cogs FLOAT, gross_margin_percentage FLOAT, gross_income FLOAT, ratig FLOAT)")    
  
# Insert data into a table

