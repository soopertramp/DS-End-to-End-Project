#import necessary libraries 
import pandas as pd
import matplotlib.pyplot as plt

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

top5_categories.plot(kind='bar', x='product_line', y='total_sales', title='Product v Sales', xlabel='Products', ylabel='Total Sales ($)')
plt.show()

#city v branch v product_line and calculates the mean total sales for each group
branch = df.groupby(['city','branch','product_line',])['total'].mean().sort_values(ascending = False)
branch

#which city has most sales
city = df.groupby(['city'])['total'].mean().sort_values(ascending = False)
city

city.plot(kind='bar', x='city', y='total', title='City v Sales', xlabel='City', ylabel='Total Sales ($)')
plt.show()

#Which payment method is the most frequent
payment = df.groupby(['payment'])['invoice_id'].count().reset_index(name='invoice_count').sort_values(by='invoice_count', ascending=False)
payment

payment.plot(kind='bar', x='payment', y='invoice_count', title='Payment v Invoice Count', xlabel='Payment Type', ylabel='No of Payments')
plt.show()

#Which type of customers are the most frequent buyers within the store
customers = df.groupby(['customer_type'])['total'].sum().reset_index(name='total_sales')
customers

customers.plot(kind='bar', x='customer_type', y='total_sales', title='Customer Type v Total Sales', xlabel='Customer Type', ylabel='Total Sales')
plt.show()

#which gender buys the most
gender = df.groupby(['gender'])['total'].sum().reset_index(name='total_sales')
gender

gender.plot(kind='bar', x='gender', y='total_sales', title='Gender v Total Sales', xlabel='Gender', ylabel='Total Sales')
plt.show()

# concatenate date and time columns
datetime_col = pd.to_datetime(df['date'] + ' ' + df['time'])

# add the new datetime column to the dataframe
df['date_time'] = datetime_col

df = df.drop(['date', 'time'], axis=1)

#checking the data types
df.dtypes

# extract the date and time components
df['date'] = df['date_time'].dt.date
df['time'] = df['date_time'].dt.time

df.set_index('date','time', inplace=True)

# df = df.drop(['date_time'], axis=1)
# df.columns

#total amount of sales per day
sales_per_day = df.groupby(['date'])['total'].sum()
sales_per_day

sales_per_day.plot(kind='line', x='date', y='total', title='Total Sales Per Day', xlabel='Date', ylabel='Total Sales Per Day ($)')
plt.show()