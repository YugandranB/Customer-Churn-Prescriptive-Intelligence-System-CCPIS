import numpy as np
import pandas as pd
import datetime as dt
from config import CHURN_THRESHOLD_DAYS

def build_behavioral_features(df):

    df = df.dropna(subset=['Customer ID'])
    df = df[~df['Invoice'].astype(str).str.contains('C', na=False)]
    df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalSum'] = df['Quantity'] * df['Price']

    country_map = df.groupby('Customer ID')['Country'].first()
    top_products = df.groupby('Customer ID')['Description'].apply(
        lambda x: x.value_counts().head(3).index.tolist()
    )

    cust_stats = df.groupby('Customer ID').agg({
        'InvoiceDate': [lambda x: (x.max() - x.min()).days, 'max', 'nunique'],
        'TotalSum': 'sum'
    })

    cust_stats.columns = ['Lifespan', 'LastDate', 'Frequency', 'Monetary']

    cust_stats['IPT'] = np.where(
        cust_stats['Frequency'] > 1,
        cust_stats['Lifespan'] / (cust_stats['Frequency'] - 1),
        cust_stats['Lifespan']
    )

    ref_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

    rfm = pd.DataFrame()
    rfm['Recency'] = (ref_date - cust_stats['LastDate']).dt.days
    rfm['Frequency'] = cust_stats['Frequency']
    rfm['Monetary'] = cust_stats['Monetary']
    rfm['IPT'] = cust_stats['IPT']
    rfm['Country'] = country_map
    rfm['Top_Products'] = top_products

    rfm['Churn'] = (rfm['Recency'] > CHURN_THRESHOLD_DAYS).astype(int)

    return rfm
