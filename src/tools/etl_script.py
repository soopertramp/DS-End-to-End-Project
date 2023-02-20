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

top5_categories.plot(kind='bar', x='product_line', y='total_sales', title='Product v Sales', xlabel='Products', ylabel='Total Sales ($)')
plt.show()

#city v branch v product_line and calculates the mean total sales for each group
branch = df.groupby(['city','branch','product_line',])['total'].mean().sort_values(ascending = False)

#which city has most sales
city = df.groupby(['city'])['total'].mean().sort_values(ascending = False)

city.plot(kind='bar', x='city', y='total', title='City v Sales', xlabel='City', ylabel='Total Sales ($)')
plt.show()

#Which payment method is the most frequent
payment = df.groupby(['payment'])['invoice_id'].count().reset_index(name='invoice_count').sort_values(by='invoice_count', ascending=False)

payment.plot(kind='bar', x='payment', y='invoice_count', title='Payment v Invoice Count', xlabel='Payment Type', ylabel='No of Payments')
plt.show()

#Which type of customers are the most frequent buyers within the store
customers = df.groupby(['customer_type'])['total'].sum().reset_index(name='total_sales')

customers.plot(kind='bar', x='customer_type', y='total_sales', title='Customer Type v Total Sales', xlabel='Customer Type', ylabel='Total Sales')
plt.show()

#which gender buys the most
gender = df.groupby(['gender'])['total'].sum().reset_index(name='total_sales')

gender.plot(kind='bar', x='gender', y='total_sales', title='Gender v Total Sales', xlabel='Gender', ylabel='Total Sales')
plt.show()

# concatenate date and time columns
datetime_col = pd.to_datetime(df['date'] + ' ' + df['time'])

# add the new datetime column to the dataframe
df['date_time'] = datetime_col

# extract the date and time components
df['date'] = df['date_time'].dt.date
df['time'] = df['date_time'].dt.time

#df.set_index('date','time', inplace=True)

# df = df.drop(['date_time'], axis=1)
# df.columns

#total amount of sales per day
sales_per_day = df.groupby(['date'])['total'].sum()

#Plotting total sales per day using line graph
sales_per_day.plot(kind='line', x='date', y='total', title='Total Sales Per Day', xlabel='Date', ylabel='Total Sales Per Day ($)')
plt.show()

#Creating hourly_date column by replacing minute, second, and microsecond with 0 and adding hour based on minutes
df['hourly_date'] = df['date_time'].apply(lambda x: x.replace(minute=0, second=0, microsecond=0) + pd.Timedelta(hours=x.minute//30))

#Grouping data by hourly date and counting total sales per hour
sales_per_hour = df.groupby(['hourly_date'])['date_time'].count().reset_index(name = 'total_sales_an_hour')

#Creating a new dataframe for January data
january_df = df[df['date_time'].dt.month == 1]

#Grouping January data by date and counting total sales per day
january_sales = january_df.groupby(['date'])['total'].count()

#Plotting total sales per day in January using line graph
january_sales.plot(kind='line', x='hourly_date', y='total', title='Total Sales Per Day in January', xlabel='Date', ylabel='Total Sales Per Day ($)')
plt.show()

#Creating a new dataframe for February data
february_df = df.loc[df['hourly_date'].dt.month == 2]

#Grouping February data by date and counting total sales per day
february_sales = february_df.groupby(['date'])['total'].count()

#Plotting total sales per day in February using line graph
february_sales.plot(kind='line', x='date', y='total', title='Total Sales Per Day in February', xlabel='Date', ylabel='Total Sales Per Day ($)')
plt.show()

#Creating a new dataframe for March data
march_df = df.loc[df['hourly_date'].dt.month == 3]

#Grouping March data by date and counting total sales per day
march_sales = march_df.groupby(['date'])['total'].count()

#Plotting total sales per day in March using line graph
march_sales.plot(kind='line', x='date', y='total', title='Total Sales Per Day in February', xlabel='Date', ylabel='Total Sales Per Day ($)')
plt.show()

#total monthly sales
monthly_sales = df.groupby(df['date_time'].dt.strftime('%Y-%m'))['total'].sum().reset_index(name = 'total_sales_for_the_month').sort_values(by = 'total_sales_for_the_month', ascending = False)

monthly_sales.plot(kind='bar', x='date_time', y='total_sales_for_the_month', title='Total Sales Per Month', xlabel='Months', ylabel='Total Sales Per Month ($)')
plt.show()