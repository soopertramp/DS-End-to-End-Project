# :man_technologist: Data Science End2End Project

## :pushpin: Project Architecture

<img src="https://github.com/soopertramp/DS-End-to-End-Project/blob/main/End2End_architecture.jpg" height="300" width="1000" />

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

## :rocket: Getting Started
To get started with this project, you'll need to clone the repository and make changes to the code. Here's how:

#### :link:  Cloning the Repository

- Go to the repository's page on Github and click the "Code" button.
- Select "HTTPS" or "SSH" as the clone method, depending on your preference.
- Copy the URL provided.
- Open a terminal or command prompt and navigate to the directory where you want to store the repository on your local machine.
- Type "git clone" followed by the URL you copied in step 3.

For example, if the repository's URL is "https://github.com/user/repo.git" and you want to store the repository in a folder called "my-project" on your desktop, you would type the following command:

``` git clone https://github.com/user/repo.git ~/Desktop/my-project ```

## :handshake: Giving Credit

If you make changes to the code, it's important to give credit to the original project's author. You can do this by adding a note or comment to your code, or by including the original author's name and a link to the project in your documentation.

For example, if you add a new feature to the code, you could include a comment like this:

``` // New feature added by [your name]. Original code by [original author name].```

``` // Link to original project: [link to original project] ```

## :computer: :memo: :thinking: Working with the Code

Once you have cloned the repository, you can start working with the code. Here are some tips to get you started:

- Read the [User Guide](https://github.com/soopertramp/DS-End-to-End-Project#open_book-user-guide) and code comments to understand how the code works.
- Make changes to the code as needed, testing your changes to ensure they work correctly.
- If you want to contribute your changes back to the original project, create a pull request on Github. Be sure to include a detailed description of your changes and why they are important or necessary.

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

## :handshake::thought_balloon: Contributing

If you would like to contribute to this project, please create a pull request on Github: [Pull Request](https://github.com/soopertramp/DS-End-to-End-Project/compare)

## :end: Conclusion

This project showcases the ability to handle real-world data and solve a problem using data science techniques. The project can be used as a reference for building similar projects in the future. Feel free to use the code and make modifications as per your requirements and don't forget to give credit.

## :bulb: Created and Contributed by

:man_technologist: [Pradeepchandra Reddy S C](https://www.linkedin.com/in/pradeepchandra-reddy-s-c/)

:man_technologist: [Data To Production (Mitul Patel Msc - Mentor)](https://www.linkedin.com/in/mitul-patel2393/)
