import pandas as pd
from typing import List, Tuple, Union

#read data using pandas

def get_data(path: str) -> pd.DataFrame:
    
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters
    ----------
    path : str
        The file path of the CSV file to be loaded.

    Returns
    -------
    pd.DataFrame
        The loaded data in a pandas DataFrame.

    """
    
    df = pd.read_csv(path)
    df.drop(columns = ['Unnamed : 0'], inplace = True, errors = 'ignore')
    return df #return gives modified data back so that it can assigned to a variable where as print cannot be assigned

df = get_data("data\\supermarket_sales.csv")
df

df.columns

df.dtypes

def create_db_schema(data: pd.DataFrame) -> Tuple[str, str]:
    types = []
    for i in df.dtypes:
        if i == 'object':
            types.append('VARCHAR(255)')
        elif i == 'float64':
            types.append('FLOAT')
        elif i == 'int64':
            types.append('INT')
    col_type = list(zip(df.columns.values, types))
    col_type = tuple([" ".join(i) for i in col_type])
    col_type = ", ".join(col_type)
    values = ', '.join(['%s' for _ in range(len(df.columns))])
    return col_type, values





