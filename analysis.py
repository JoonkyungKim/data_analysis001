import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    return df

def get_summary_stats(df):
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nTop Genres:")
    print(df['listed_in'].value_counts().head(5))
