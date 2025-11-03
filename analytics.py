import pandas as pd

def calculate_metrics(df):
    df['Daily Return'] = df['Close'].pct_change()
    avg_close = df['Close'].mean()
    volatility = df['Daily Return'].std()
    return {
    "Average Close Price": float(round(df['Close'].mean(), 2)),
    "Volatility": float(round(df['Daily Return'].std() * 100, 2))
}
