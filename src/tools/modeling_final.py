from typing import List

import gspread
import matplotlib.pyplot as plt
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from prophet import Prophet

from src.tools.utils import read_file_from_s3
from src.tools.utils import upload_to_google_sheet

# Read the file from S3 bucket into a pandas DataFrame
data = read_file_from_s3('supermarket_cleaned.csv')

def generate_forecasts(df: pd.DataFrame, cities: List[str], product_lines: List[str]) -> pd.DataFrame:
    """
    Generates sales forecasts for a list of cities and product lines using the Prophet library.

    Parameters:
    -----------
    df : pandas DataFrame
        A DataFrame containing sales data.
    cities : list of str
        A list of cities for which forecasts are to be generated.
    product_lines : list of str
        A list of product lines for which forecasts are to be generated.
        
    Returns:
    --------
    pandas DataFrame
        A DataFrame containing the forecasted dates, as well as the predicted lower, upper, and mean values for each
        combination of city and product line.
        - city: The name of the city for which sales were forecasted.
        - product_line: The name of the product line for which sales were forecasted.
        - ds: A datetime object representing the date.
        - yhat: A float representing the predicted sales value.
    """   
    # Initialize an empty list to store the forecasts
    forecasts = []

    # Loop through each city and product line to generate forecasts
    for city in cities:
        for product_line in product_lines:
            # Filter the DataFrame based on the city and product line
            filter = df[(df['city'] == city) & (df['product_line'] == product_line)]
            
            # Rename the 'date' and 'quantity' columns to 'ds' and 'y', respectively
            filter = filter[['date', 'quantity']].rename(columns={'date': 'ds', 'quantity': 'y'})
            
            # Create a new Prophet object
            model = Prophet()

            # Fit the model to the data
            model.fit(filter)

            # Create a new DataFrame for the future dates
            future_dates = model.make_future_dataframe(periods=60)

            # Generate predictions for the future dates
            forecast = model.predict(future_dates)

            # Add the city and product line as columns to the forecast DataFrame
            forecast['city'] = city
            forecast['product_line'] = product_line

            # Append the forecast to the list of forecasts
            forecasts.append(forecast[['city', 'product_line', 'ds', 'yhat']])

    # Concatenate all of the forecasts into a single DataFrame
    forecasts_df = pd.concat(forecasts, ignore_index=True)
    
    return forecasts_df

# Get unique cities and product lines from the data
cities = data['city'].unique()
product_lines = data['product_line'].unique()

# Generate sales forecasts for all combinations of cities and product lines
predictions = generate_forecasts(data, cities, product_lines)

upload = upload_to_google_sheet('1d9qOwKAaOVdkyuubjCycIcPO_H7ASbUkk_tN75JF2go', predictions, 'Sheet1')