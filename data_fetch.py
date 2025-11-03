import yfinance as yf
import pandas as pd

def fetch_history(ticker, period='1y', interval='1d'):
    t = yf.Ticker(ticker)
    df = t.history(period = period, interval = interval)
    df = df.reset_index()
    df = df[['Date', 'Close']]
    df['Ticker'] = ticker
    return df

