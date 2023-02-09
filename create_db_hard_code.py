#importing the MySQL Connector library

import mysql.connector as mysql

#establish a connection to the database

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

#executing "SHOW DATABASES" shows the databases on your computer

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
  
#create a database

mycursor.execute("CREATE DATABASE IF NOT EXISTS supermarket")

#checking if that works

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
  
#use database

mycursor.execute("USE supermarket")

#drop table

mycursor.execute("DROP TABLE supermarket_sales")
  
#create a table

mycursor.execute("CREATE TABLE supermarket_sales (invoice_id VARCHAR(255), branch CHAR, city VARCHAR(255), customer_type VARCHAR(255), gender VARCHAR(255), product_line VARCHAR(255), unit_price FLOAT, quantity INT, tax_5_percent FLOAT, total FLOAT, date DATE, time TIME, payment VARCHAR(255), cogs FLOAT, gross_margin_percentage FLOAT, gross_income FLOAT, rating FLOAT)")    
  
#insert data into a table

import csv

with open('supermarket_sales.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Loop through each row in the CSV file
    for row in reader:
        # Create the INSERT INTO SQL statement
        sql = "INSERT INTO supermarket_sales (invoice_id, branch, city, customer_type, gender, product_line, unit_price, quantity, tax_5_percent, total, date, time, payment, cogs, gross_margin_percentage, gross_income, rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Execute the SQL statement
        mycursor.execute(sql, row)
        
#commit the transaction
mydb.commit()

#retrieve data from a table
mycursor.execute("select * from supermarket_sales")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
mydb.close()





































#cleaning the date column

query = "SELECT date FROM supermarket_sales"
mycursor.execute(query)
dates = mycursor.fetchall()

# clean the date values in the column

cleaned_dates = []
for date in dates:
    cleaned_date = date[0].strftime("%Y-%m-%d")
    cleaned_dates.append(cleaned_date)
    
# update the cleaned date values in the MySQL table

for i, cleaned_date in enumerate(cleaned_dates):
    update_query = "UPDATE supermarket_sales SET date = %s WHERE id = %s"
    mycursor.execute(update_query, (cleaned_date, i+1))
    
mydb.commit()