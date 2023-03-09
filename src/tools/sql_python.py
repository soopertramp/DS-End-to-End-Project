import mysql.connector as mysql
import pandas as pd
from pathlib import Path
from src.tools.utils import authenticate_s3
from src.tools.utils import upload_to_s3

auth,buck = authenticate_s3()

def run_sql_script(database: str, script_path: Path) -> pd.DataFrame:
    """Runs an SQL script and returns the result as a pandas DataFrame.

    Args:
        database (str): Name of the database to connect to.
        script_path (Path): Path to the SQL script file.

    Returns:
        pd.DataFrame: Result of the SQL script as a pandas DataFrame.

    """
    # Create a connection to the database
    db = mysql.connect(
        host='localhost',
        user='root',
        password='password',
        database=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Open the SQL file and read its contents
    with open(script_path, 'r') as file:
        sql_script = file.read()

    # Execute the SQL script using the cursor object
    cursor.execute(sql_script)
    cursor.fetchall()
    
    # Read the result into a pandas dataframe
    df = pd.read_sql(sql_script, db)

    # Close the database connection
    db.close()

    return df

def process():
    database = 'cleaned_supermarket'
    script_path = Path('src/tools/merge_query.sql')
    df = run_sql_script(database, script_path)
    return df
