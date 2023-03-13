import argparse
import os
import yaml
from pathlib import Path

import mysql.connector as mysql
from dotenv import load_dotenv
from mysql.connector import Error
from utils import (connect_to_mysql, create_database, create_db_schema,
                   create_table, get_data)

#Extract the arguments
parser = argparse.ArgumentParser(description='Connects to a MySQL database and creates a table with data from an input CSV file')
parser.add_argument('-cd', '--create_db', type=bool, default=False, help='Whether to create the database (True or False)')
parser.add_argument('-nd', '--name_the_db', type=str, help='The name of the database', required=True)
parser.add_argument('-id', '--task_id', type=str, help='The tasks defined in the config files.')
args = parser.parse_args()

# load tasks from config --------------------------------------------------------------
with open("./config/config.yaml", 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

#read mysql password
env_path = Path('.env')
load_dotenv(env_path)
password = os.getenv('password')

# connect to mysql
mydb, cursor = connect_to_mysql(host='localhost', user='root', password=password)

if args.create_db:
    databases = create_database(cursor, args.name_the_db)
    print(databases)
else:
    # define variables
    config_import = config[args.task_id]["import"]
    for i in range(len(config_import)):
        data = Path(config_import[i]["import"]["dirpath"], 
                config_import[i]["import"]["prefix_filename"]+ '.' +
                config_import[i]["import"]["file_extension"])
        table_name = os.path.basename(data).split('.')[0]
        df = get_data(data)
        col_type, values = create_db_schema(df)
        create_table(args.name_the_db, table_name, col_type, cursor)
        # create the schema for the database using the create_db_schema() function 
        for i,row in df.iterrows():
            # create an SQL query string for each row using the values list and the table name
            # and execute it using the cursor object 
            sql = f"INSERT INTO {table_name} VALUES ({values})"
            cursor.execute(sql, tuple(row))
            # commit the changes to the database
            mydb.commit()
        # print the number of records inserted
        print(cursor.rowcount, "Record inserted")    

cursor.close()
mydb.close()