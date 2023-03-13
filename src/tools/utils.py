# import necessary libraries
import importlib
import os
from io import StringIO
from pathlib import Path
from typing import List, Optional, Tuple

import boto3
import gspread
import mysql.connector as mysql
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


# Define a function that connects to a MySQL server and creates a cursor object.
def connect_to_mysql(host: str, user: str, password: str) -> Tuple[mysql.connection.MySQLConnection, mysql.cursor.MySQLCursor]:
    """
    Connects to a MySQL server with the given hostname, username, and password.

    Parameters:
    -----------
        host: str 
            The hostname of the MySQL server to connect to.
        user: str 
            The username to use when connecting to the server.
        password: str
            The password to use when connecting to the server.

    Returns:
    --------
        Tuple[mysql.connection.MySQLConnection, mysql.cursor.MySQLCursor]
            A tuple containing two objects: the connection to the MySQL server and a cursor object.
        The cursor can be used to execute SQL statements and retrieve results from the server.

    Raises:
    -------
        Exception: If an error occurs while connecting to the MySQL server.
    """
    env_path = Path('.env')
    load_dotenv(env_path)
    try:
        # connect to MySQL
        mydb = mysql.connect(
            host = host,
            user = user,
            password = os.getenv('password')
        )
        print("Connected to MySQL successfully!")
        
        # create a cursor
        cursor = mydb.cursor()
        print("Cursor object created successfully!")
    except Exception as e:
        print("Error: ", e)        
    return mydb, cursor

# Define a function that creates a new MySQL database.        
def create_database(cursor: mysql.cursor.MySQLCursor, database_name: str) -> List:
    """
    Creates a new MySQL database with the given name.

    Parameters:
    -----------
    cursor : mysql.cursor.MySQLCursor
        The cursor object to use to execute SQL statements.
    database_name : str
        The name of the new database to create.

    Returns:
    --------
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
    return databases

# Define a function that creates a new MySQL table.        
def create_table(database_name: str, table_name: str, col_type: str, cursor: mysql.cursor.MySQLCursor):
    """
    Create a new MySQL table with the given name, using the specified column names and data types.

    Parameters
    ----------
    database_name : str
        The name of the database in which to create the new table.
    table_name : str
        The name of the new table to create.
    col_type : str
        A string specifying the column names and data types for the new table.
    cursor : mysql.cursor.MySQLCursor
        The cursor object to use to execute SQL statements.

    Returns
    -------
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

    Parameters
    ----------
    path : str
        The path to the CSV file to be loaded.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame containing the data from the CSV file.
    """
    # Load data from CSV file
    df = pd.read_csv(path)
    # Drop the 'Unnamed : 0' column, if it exists
    df.drop(columns = ['Unnamed : 0'], inplace = True, errors = 'ignore')
    return df 

# Define a function that creates sql schema and values for a table
def create_db_schema(df: pd.DataFrame) -> Tuple[str, str]:
    """
    Given a pandas DataFrame `data`, this function returns a tuple of two strings representing 
    the SQL schema and placeholder values for a table in a relational database.

    Parameters:
    -----------
    df : pandas.DataFrame
        The pandas DataFrame to upload.

    Returns:
    --------
    - Tuple[str, str]: A tuple of two strings, the first one represents the SQL schema, and the 
    second one represents the placeholder values for the table. 
    """
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

# Define a function to Authenticate AWS and set up an S3 client
def authenticate_s3() -> Tuple[boto3.client, str]:
    """
    Authenticates with AWS and sets up an S3 client using environment variables.

    Returns:
    --------
    tuple
        A tuple containing an S3 client object and the bucket name that can be used to interact with an S3 bucket.

    Notes:
    ------
    This function requires AWS credentials to be stored in a file named '.env' in the same directory as this script. The '.env' file should contain the following variables:
    - access_key_id: The Access Key ID for your AWS account.
    - secret_access_key: The Secret Access Key for your AWS account.
    - region: The AWS region where your S3 bucket is located.
    - bucket_name: The name of the S3 bucket that you want to interact with.
    """
    env_path = Path('.env')
    load_dotenv(env_path)
    client = boto3.client('s3', aws_access_key_id=os.getenv('access_key_id'), 
                          aws_secret_access_key=os.getenv('secret_access_key'), 
                          region_name=os.getenv('region'))

    bucket_name = os.getenv('bucket_name')
    
    # Return the S3 client and bucket name as a tuple
    return client, bucket_name

# Define a function to Upload a file to an S3 bucket
def upload_to_s3(df: pd.DataFrame, filename: str) -> bool:
    """
    Uploads a pandas DataFrame to an S3 bucket.

    Parameters:
    -----------
    df : pandas.DataFrame
        The pandas DataFrame to upload.

    filename : str
        The name to give to the uploaded file. This should not include the file extension.

    Returns:
    --------
    bool
        True if the DataFrame was successfully uploaded, False otherwise.
    """
    # Authenticate with AWS
    client, bucket_name = authenticate_s3()

    # Upload the file
    try:
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        response = client.put_object(
            ACL = 'private',
            Body=csv_buffer.getvalue(),
            Bucket = bucket_name,
            Key=filename + '.csv'
        )
    except Exception as e:
        print(e)
        return False
    return True

# Define a function to read a file from an S3 bucket and return its contents as a dataframe
def read_file_from_s3(file_name: str) -> pd.DataFrame:
    """
    Read a file from an Amazon S3 bucket and return its contents as a pandas DataFrame.

    Parameters:
    -----------
    file_name : str
        The name of the file to read from the S3 bucket.

    Returns:
    --------
    df : pandas.DataFrame or None
        The contents of the file as a pandas DataFrame, or None if the file could not be read.

    Raises:
    -------
    Exception
        If an error occurs during the read process.
    """
    # Authenticate with AWS
    s3, bucket_name = authenticate_s3()

    # Read the file
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        df = pd.read_csv(response['Body'])
    except Exception as e:
        # If an exception occurs during the read process, print the error message and return None
        print(e)
        return None
    
    # Return the dataframe
    return df
      
# Define a function to Upload a file to a Google Sheet
def upload_to_google_sheet(spreadsheet_id: str, df: pd.DataFrame, worksheet_name: str) -> bool:
    """
    Uploads a pandas DataFrame to a Google Sheet.

    Parameters:
    -----------
    spreadsheet_id : str
        The ID of the Google Sheet to upload the DataFrame to.

    df : pandas.DataFrame
        The pandas DataFrame to upload.

    worksheet_name : str
        The name of the worksheet within the Google Sheet to upload the DataFrame to.

    Returns:
    --------
    bool
        True if the DataFrame was successfully uploaded, False otherwise.

    """
    # Authenticate with Google Sheets API
    
    SCOPES = [
        "https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name("GCP.json", SCOPES)
    gc = gspread.authorize(credentials)

    # Open the worksheet
    try:
        worksheet = gc.open_by_key(spreadsheet_id).worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = gc.open_by_key(spreadsheet_id).add_worksheet(worksheet_name, 1, 1)

    # Clear the existing content in the worksheet
    worksheet.clear()

    # Convert Timestamp columns to string format
    df = df.astype(str)

    # Write the DataFrame to the worksheet
    cell_list = worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    if cell_list:
        return True
    else:
        return False
    
def process_task(task: str) -> dict:
    """Import task file to process the data from src/tools folder
    Args:
        task (str): name of the task to process
    Returns:
        dict: processed_data
    """
    lib = importlib.import_module(f"src.tools.{task}")
    return lib.process()