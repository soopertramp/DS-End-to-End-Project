import pandas as pd

#read data using pandas

def get_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.drop(columns = ['Unnamed : 0'], inplace = True, errors = 'ignore')
    return df #return gives modified data back so that it can assigned to a variable where as print cannot be assigned

df = get_data("data\\supermarket_sales.csv")
df

