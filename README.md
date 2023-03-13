# :man_technologist: Data Science End2End Project

[embed]https://github.com/soopertramp/DS-End-to-End-Project/blob/main/End2End.pdf[/embed]

## :wave: Introduction

This repository contains an end-to-end data science project that demonstrates the complete data science process from data collection to deployment. The project aims to provide insights into a real-world problem and solve it using data science techniques.

## :memo: Project Description

The project is focused on forecasting quantity for a supermarket. The data used in this project has been collected from [data source]. The data has been cleaned, preprocessed and analyzed to obtain insights and to build a predictive model. The predictive model has been built using facebook's prophet algorithm. The model has then been deployed using Jenkins and Looker Studio, formerly Google Data Studio.

## :briefcase: :pencil: Requirements

| library | Description |
|---------| ----------- |
|`mysql-connector-python`| A library that provides connectivity to MySQL databases.|
|`matplotlib`| A plotting library for creating visualizations in Python|
|`pandas`| A library for data manipulation and analysis.|
`python-dotenv`| A library for working with environment variables stored in a .env file.
`pathlib`| A library for working with file system paths.
`argparse`| A library for parsing command line arguments.
`os`| A library for interacting with the operating system.
`yaml`| A library for parsing YAML files.
`typing`| A library for supporting type hints in Python.
`gspread`| A library for working with Google Sheets.
`oauth2client.service_account`| A library for authenticating with Google APIs using a service account.
`prophet`| A library for time series forecasting developed by Facebook.
`io`| A library for working with I/O streams.
`importlib`| A library for programmatically importing modules.
`boto3`| A library for interacting with AWS services using Python.
`googleapiclient.discovery`| A library for discovering and using Google APIs.

## :open_book: User Guide

#### STEP - :one: : Navigate to the project directory in the terminal by running 

```cd " YOUR FOLDER LOCATION "``` 

#### This step is necessary to ensure that you are in the correct directory where the project files are located.

#### STEP - :two: : Activate the project environment by running 

```conda activate End2End``` 

#### This step is necessary to activate the Conda environment that contains all the required [libraries and dependencies](https://github.com/soopertramp/DS-End-to-End-Project/blob/main/requirements.txt) for the project.

#### STEP - :three: : Create the database by running the below code 

```python src\tools\database_final.py -cd True -nd "YourDatabaseName"``` 

#### This step creates the database with the specified name. The -cd argument specifies whether to create or drop the database, and -nd specifies the name of the database.

#### STEP - :four: : Load the data into the database by running 

```python src\tools\database_final.py -nd "YourDatabaseName" -id upload-to-database```

#### This step loads the raw data into the database. The -nd argument specifies the name of the database, and -id specifies the operation to be performed (in this case, uploading data to the database).

#### STEP - :five: : Run the ETL script to transform the data by running 

```python src\tools\etl_script_final.py```

#### This step performs the ETL (Extract-Transform-Load) process to transform the raw data into a format suitable for modeling.

#### STEP - :six: : Create the cleaned database by running 

```python src\tools\database_final.py -cd True -nd "CleanedDatabaseName"``` 

#### This step creates a new database with the cleaned data.

#### STEP - :seven: : Load the cleaned data into the database by running 

```python src\tools\database_final.py -nd "CleanedDatabaseName" -id cleaned-upload-to-database``` 

#### This step loads the cleaned data into the database.

#### STEP - :eight: : Run SQL queries from Python Script on the database by running 

```python src\tools\sql_python.py``` 

#### This step allows you to run SQL queries on the database and retrieve specific data based on your needs.

#### STEP - :nine: : Run main.py with task parameter 

```python main.py -t sql_python``` 

#### This will execute the "main.py" script with the "sql_python" task parameter, triggering the SQL query and export process resulting output file (df) should be uploaded to the specified S3 bucket after the script completes execution.

#### STEP - :keycap_ten: : Run the final modeling script by running the code 

```python main.py -t modeling_final``` 

#### This step runs the final modeling script to build a predictive model based on the cleaned data. The -t argument specifies the type of script to run, and "modeling_final" is the name of the script and uploads the Predictions to a Google Sheet

## :end: Conclusion

This project showcases the ability to handle real-world data and solve a problem using data science techniques. The project can be used as a reference for building similar projects in the future. Feel free to use the code and make modifications as per your requirements and don't forget to give credit.

## :bulb: Created and Contributed by

:man_technologist: [Pradeepchandra Reddy S C](https://www.linkedin.com/in/pradeepchandra-reddy-s-c/)

:man_technologist: [Data To Production (Mitul Patel Msc - Mentor)](https://www.linkedin.com/in/mitul-patel2393/)
