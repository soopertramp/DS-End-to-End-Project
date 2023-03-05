from src.tools.utils import upload_to_s3
from src.tools.utils import read_file_from_s3

data = upload_to_s3('data\supermarket_sales.csv', 'supermarket_sales.csv')

df = read_file_from_s3(file_name = 'supermarket_sales.csv')

yangon_sales = df[df['city'] == 'Yangon']

food = yangon_sales[yangon_sales['product_line'] == 'Food and beverages']