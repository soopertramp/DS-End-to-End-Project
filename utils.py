# import necessary libraries
import pandas as pd
from typing import List, Tuple, Union
import mysql.connector as mysql

# Define a function that connects to a MySQL server and creates a cursor object.
def connect_to_mysql(host: str, user: str, password: str) -> Tuple[mysql.connection.MySQLConnection, mysql.cursor.MySQLCursor]:
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

# Define a function that creates a new MySQL database.        
def create_database(cursor: cursor, database_name: str) -> None:
    """
    Creates a new MySQL database with the given name.

    Args:
        cursor (cursor): The cursor object to use to execute SQL statements.
        database_name (str): The name of the new database to create.

    Returns:
        None
    """
    # Drop the database if it already exists
    drop_db_query = f'DROP DATABASE IF EXISTS {database_name}'
    cursor.execute(drop_db_query)

    # Create the database
    create_db_query = f'CREATE DATABASE {database_name}'
    cursor.execute(create_db_query)

    # Show all databases on the MySQL server
    cursor.execute('SHOW DATABASES')
    databases = cursor.fetchall()
    print("List of databases:")
    for db in databases:
        print(db[0])

# Define a function that creates a new MySQL table.        
def create_table(database_name: str, table_name: str, col_type: str, cursor: mysql.cursor.MySQLCursor) -> None:
    """
    Creates a new MySQL table with the given name, using the specified column names and data types.

    Args:
        database_name (str): The name of the database in which to create the new table.
        table_name (str): The name of the new table to create.
        col_type (str): A string specifying the column names and data types for the new table.
        cursor (mysql.cursor.MySQLCursor): The cursor object to use to execute SQL statements.

    Returns:
        None
    """
    # Connect to the MySQL server and select the specified database
    cursor.execute(f'USE {database_name}')

    # Drop the table if it already exists
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')

    # Create a new table with the specified columns and data types
    cursor.execute(f"CREATE TABLE {table_name} ({col_type})")

# Define a function that loads data from a CSV file into a pandas DataFrame.
def get_data(path: str) -> pd.DataFrame:
    """
    Loads data from a CSV file into a pandas DataFrame.

    Args:
        path (str): The path to the CSV file to be loaded.

    Returns:
        pd.DataFrame: A pandas DataFrame
    """
    # Load data from CSV file
    df = pd.read_csv(path)
    # Drop the 'Unnamed : 0' column, if it exists
    df.drop(columns = ['Unnamed : 0'], inplace = True, errors = 'ignore')
    return df 

# Define a function that creates sql schema and values for a table
def create_db_schema(data: pd.DataFrame) -> Tuple[str, str]:
    """
    Given a pandas DataFrame `data`, this function returns a tuple of two strings representing 
    the SQL schema and placeholder values for a table in a relational database.

    Args:
    - data (pd.DataFrame): The input pandas DataFrame.

    Returns:
    - Tuple[str, str]: A tuple of two strings, the first one represents the SQL schema, and the 
    second one represents the placeholder values for the table. """
    # Determine the SQL data type for each column in the DataFrame
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
