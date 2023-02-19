import argparse
import os
from pathlib import Path

import mysql.connector as mysql
from dotenv import load_dotenv
from mysql.connector import Error
from utils import create_db_schema, get_data

#Extract the arguments
parser = argparse.ArgumentParser()
parser.add_argument('-db', '--create_db', help = 'create db or not', default = False, type = bool)
parser.add_argument('-db_name', '--db_name', help = 'database name', default = False, type = bool)
parser.add_argument('-t', '--task', help = 'this will point to a task location into the \
                    config.yaml file.', type = str)

args = parser.parse_args()

#Load the tasks from config


#read mysql password

#create a databse
if args.create_db:
    try:
        conn = mysql.connect(host = 'localhost', user = 'root', password = 'password')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(f'DROP DATABASE IF EXISTS {args.db_name}')
            print(f'Database is created: {args.db_name}')
            cursor.execute('SHOW DATABSES')
            record = cursor.fetchall()
            print('Databases exist: ', record)
    except Error as e:
        print('Error while connecting to MySQL', e)
#create a table in database
else:
    #loop through eachtask in config.yams
    #args task = 'cleaned_cdv_to_databse'
    config_import = config[args.task]['import']       
