from src.tools.utils import authenticate_s3
from src.tools.utils import upload_to_s3
from src.tools.utils import read_file_from_s3
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

authenticate_s3()

# Read the file from S3 bucket into a pandas DataFrame
df = read_file_from_s3(file_name = 'supermarket_sales_cleaned.csv')

# Filter the DataFrame based on specific conditions
filter = df[(df['city'] == 'Yangon') & (df['product_line'] == 'Food and beverages')]

# Rename the 'date' and 'total' columns to 'ds' and 'y', respectively
filter = filter.rename(columns = {'date' : 'ds', 'total' : 'y'})

# Create a new DataFrame with only the 'ds' and 'y' columns
food = filter[['ds', 'y']]

# Create a new Prophet object
m = Prophet()

# Fit the model to the data
m.fit(food)

# Create a new DataFrame for the future dates
future = m.make_future_dataframe(periods=365)

# Show the last few rows of the future DataFrame
future.tail()

# Generate predictions for the future dates
forecast = m.predict(future)

# Show the last few rows of the forecast DataFrame
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

# Plot the forecasted values
fig1 = m.plot(forecast)
plt.title('Food and Beverages Forecast - Yangon')
plt.show()

# Plot the individual components of the forecast
fig2 = m.plot_components(forecast)
plt.title('Food and Beverages Forecast Components - Yangon')
plt.show()

# function that can be used to predict sales for different cities and product lines
def predict_sales(city: str, product_line: str) -> pd.DataFrame:
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
    # Read the file from S3 bucket into a pandas DataFrame
    df = read_file_from_s3(file_name = 'supermarket_sales_cleaned.csv')

    # Filter the DataFrame based on specific conditions
    filter = df[(df['city'] == city) & (df['product_line'] == product_line)]

    # Rename the 'date' and 'total' columns to 'ds' and 'y', respectively
    filter = filter.rename(columns = {'date' : 'ds', 'total' : 'y'})

    # Create a new DataFrame with only the 'ds' and 'y' columns
    sales = filter[['ds', 'y']]

    # Create a new Prophet object
    m = Prophet()

    # Fit the model to the data
    m.fit(sales)

    # Create a new DataFrame for the future dates
    future = m.make_future_dataframe(periods=365)

    # Generate predictions for the future dates
    forecast = m.predict(future)

    # Plot the forecasted values
    fig1 = m.plot(forecast)
    plt.title(f'{product_line} Category Forecast - {city}')
    plt.show()

    # Plot the individual components of the forecast
    fig2 = m.plot_components(forecast)
    plt.title(f'{product_line} Category Forecast Components - {city}')
    plt.show()
    
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]