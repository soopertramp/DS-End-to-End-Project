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

mycursor.execute("USE supermarket")

#drop table

mycursor.execute("DROP TABLE supermarket_sales")
  
# Create a table

mycursor.execute("CREATE TABLE supermarket_sales (invoice_id INT, branch CHAR, city VARCHAR(255), customer_type VARCHAR(255), gender VARCHAR(255), product_line VARCHAR(255), unit_price FLOAT, quantity INT, tax_5_percent FLOAT, total FLOAT, date DATE, time TIME, payment VARCHAR(255), cogs FLOAT, gross_margin_percentage FLOAT, gross_income FLOAT, rating FLOAT)")    
  
# Insert data into a table

import csv

with open('supermarket_sales.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Loop through each row in the CSV file
    for row in reader:
        # Create the INSERT INTO SQL statement
        sql = "INSERT INTO supermarket_sales (invoice_id, branch, city, customer_type, gender, product_line, unit_price, quantity, tax_5_percent, total, date, time, payment, cogs, gross_margin_percentage, gross_income, rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Execute the SQL statement
        mycursor.execute(sql, row)