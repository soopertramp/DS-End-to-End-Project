from src.tools.utils import authenticate_s3
from src.tools.utils import upload_to_s3
from src.tools.utils import read_file_from_s3
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Read the file from S3 bucket into a pandas DataFrame
data = read_file_from_s3('supermarket_cleaned.csv')

# function that can be used to predict quantity for different cities and product lines
def predict_sales(df: pd.DataFrame, city: str, product_line: str) -> pd.DataFrame:
    """Parameters:
    -----------
    city : str
        The name of the city for which sales are to be predicted.
        
    product_line : str
        The product line for which sales are to be predicted.
        
    Returns:
    --------
    pandas DataFrame
        A DataFrame containing the forecasted dates, as well as the predicted lower, upper, and mean values.
        - ds: A datetime object representing the date.
        - yhat: A float representing the predicted sales value.
        - yhat_lower: A float representing the lower bound of the predicted sales value.
        - yhat_upper: A float representing the upper bound of the predicted sales value.
    """

    # Filter the DataFrame based on specific conditions
    filter = df[(df['city'] == city) & (df['product_line'] == product_line)]

    # Rename the 'date' and 'total' columns to 'ds' and 'y', respectively
    filter = filter[['date', 'quantity']].rename(columns = {'date' : 'ds', 'quantity' : 'y'})

    # Create a new Prophet object
    m = Prophet()

    # Fit the model to the data
    m.fit(filter)

    # Create a new DataFrame for the future dates
    future = m.make_future_dataframe(periods=60)

    # Generate predictions for the future dates
    forecast = m.predict(future)
    
    return forecast[['ds', 'yhat']]

predicted = predict_sales(df, 'Yangon', 'Food and beverages')

stores = df['city'].unique()
products = df['product_line'].unique()

forecast=[]

for c in stores:
    for p in products:
        prediction = predict_sales(df, c, p)
        forecast['city_name'] = c
        forecast['product_name'] = p
        print(prediction, c, p)
        forecast.append(prediction)

def forecast_quantity(df, city, product):
    store_product_df = df[(df['city'] == city) & (df['product_line'] == product)]
    store_product_df = store_product_df[['date', 'quantity']].rename(columns={'date': 'ds', 'quantity': 'y'})
    model = Prophet()
    model.fit(store_product_df)
    future_dates = model.make_future_dataframe(periods=60)
    forecast = model.predict(future_dates)
    return forecast[['ds', 'yhat']]        

# Getting unique stores and products
stores = df['city'].unique()
products = df['product_line'].unique()
# Looping through each store and product to generate forecasts
forecasts = []
for store in stores:
    for product in products:
        forecast = predict_sales(df, store, product)
        forecast['store'] = store
        forecast['product'] = product
        forecasts.append(forecast)

# Combining all forecasts into a single DataFrame
forecasts_df = pd.concat(forecasts, ignore_index=True)

from src.tools.utils import upload_to_google_sheet

upload_to_google_sheet('1d9qOwKAaOVdkyuubjCycIcPO_H7ASbUkk_tN75JF2go', forecasts_df, True)
 
