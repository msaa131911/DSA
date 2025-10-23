#missing value filled
import pandas as pd
import numpy as np

def clean_col_names(df):
    df.columns = df.columns.str.lower()
    return df
def fill_missing(df, column, value):
    df[column] = df[column].fillna(value)
    return df
df = pd.DataFrame({'Name': ['A', 'B'], 'Age': [20, np.nan]})
df_cleaned = (df
              .pipe(clean_col_names)
              .pipe(fill_missing, column='age', value=25)
             )

print(df_cleaned)