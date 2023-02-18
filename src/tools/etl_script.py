#import necessary libraries 
import pandas as pd

#reading the data
df = pd.read_csv('data/supermarket_sales.csv')
df.head()

#checking the data types
df.dtypes

#Checking the summary of the DataFrame
df.info()

#calculates the number of null values in each column of the DataFrame
df.isnull().sum()

#calculates the number of duplicate rows in the DataFrame
df.duplicated().sum()

#displays descriptive statistics for each numeric column in the DataFrame
df.describe()

#displays a list of the column names in the DataFrame
df.columns

#displays the unique values in the 'city' column of the DataFrame
df['city'].unique()

#displays the unique values in the 'branch' column of the DataFrame
df['branch'].unique()

#displays the unique values in the 'customer_type' column of the DataFrame
df['customer_type'].unique()

#displays the unique values in the 'payment' column of the DataFrame
df['payment'].unique()

#displays the unique values in the 'rating' column of the DataFrame
df['rating'].unique()

#displays the unique values in the 'product_line' column of the DataFrame
df['product_line'].unique()

#top 5 selling categories
top5_categories = df.groupby(['product_line'])['total'].mean().reset_index(name='total_sales').sort_values(by = 'total_sales', ascending = False)
top5_categories

#city v branch v product_line and calculates the mean total sales for each group
branch = df.groupby(['city','branch','product_line',])['total'].mean().sort_values(ascending = False)
branch

#which city has most sales
city = df.groupby(['city'])['total'].mean().sort_values(ascending = False)
city

#Which payment method is the most frequent
payment = df.groupby(['payment'])['invoice_id'].count().reset_index(name='invoice_count').sort_values(by='invoice_count', ascending=False)
payment

#Who are the most frequent buyers within the store
customers = df.groupby(['customer_type'])['total'].sum().reset_index(name='total_sales')
customers

#whcih gender buys the most
gender = df.groupby(['gender'])['total'].sum().reset_index(name='total_sales')
gender

#converting date from object to date type datatype
df['date'] = pd.to_datetime(df['date'])

df['time'] = pd.to_datetime(df['time'])

# concatenate date and time columns
datetime_col = pd.to_datetime(df['date'] + ' ' + df['time'])

# add the new datetime column to the dataframe
df['datetime'] = datetime_col

#checking the data types
df.dtypes

df['time']