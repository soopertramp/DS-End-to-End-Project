from typing import List, Tuple, Union

import mysql.connector as mysql
import pandas as pd

#function that connects to MySQL and creates a cursor object

def connect_to_mysql(host, user, password):
    """
    Connects to a MySQL server with the given hostname, username, and password.

    Args:
        host (str): The hostname of the MySQL server to connect to.
        user (str): The username to use when connecting to the server.
        password (str): The password to use when connecting to the server.

    Returns:
        A tuple containing two objects: the connection to the MySQL server and a cursor object.
        The cursor can be used to execute SQL statements and retrieve results from the server.

    Raises:
        Exception: If an error occurs while connecting to the MySQL server.
    """
    try:
        # connect to MySQL
        mydb = mysql.connect(
            host = host,
            user = user,
            password = password
        )
        print("Connected to MySQL successfully!")
        
        # create a cursor
        cursor = mydb.cursor()
        print("Cursor object created successfully!")
        
        return mydb, cursor
    except Exception as e:
        print("Error: ", e)

#function that creats database
        
def create_database(cursor, database_name):
    # drop database if exists
    drop_db_query = f'DROP DATABASE IF EXISTS {database_name}'
    cursor.execute(drop_db_query)

    # create database
    create_db_query = f'CREATE DATABASE {database_name}'
    cursor.execute(create_db_query)

    # show databases
    cursor.execute('SHOW DATABASES')
    databases = cursor.fetchall()
    print("List of databases:")
    for db in databases:
        print(db[0])

#function that read data using pandas

def get_data(path: str) -> pd.DataFrame:
    
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters
    ----------
    path : str
        The file path of the CSV file to be loaded.

    Returns
    -------
    pd.DataFrame
        The loaded data in a pandas DataFrame.

    """
    
    df = pd.read_csv(path)
    df.drop(columns = ['Unnamed : 0'], inplace = True, errors = 'ignore')
    return df 

#function that returns a tuple of two strings representing the SQL schema

def create_db_schema(data: pd.DataFrame) -> Tuple[str, str]:
    
    """
    Given a pandas DataFrame `data`, this function returns a tuple of two strings representing 
    the SQL schema and placeholder values for a table in a relational database.

    Args:
    - data (pd.DataFrame): The input pandas DataFrame.

    Returns:
    - Tuple[str, str]: A tuple of two strings, the first one represents the SQL schema, and the 
    second one represents the placeholder values for the table. """
    
    types = []
    for i in df.dtypes:
        if i == 'object':
            types.append('VARCHAR(255)')
        elif i == 'float64':
            types.append('FLOAT')
        elif i == 'int64':
            types.append('INT')
            
    # Combine column names and data types into a string of SQL schema
    col_type = list(zip(df.columns.values, types))
    col_type = tuple([" ".join(i) for i in col_type])
    col_type = ", ".join(col_type)
    
    # Create a string of placeholder values for SQL queries
    values = ', '.join(['%s' for _ in range(len(df.columns))])
    
    return col_type, values