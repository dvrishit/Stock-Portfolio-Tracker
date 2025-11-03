import streamlit as st
import matplotlib.pyplot as plt
from data_fetch import fetch_history
from analytics import calculate_metrics

st.set_page_config(page_title="Stock Portfolio Tracker", layout="centered")

st.title("📈 Stock Portfolio Tracker")
st.write("Enter a stock symbol below to fetch its data and analyze performance.")

symbol = st.text_input("Stock Symbol (e.g., AAPL, MSFT, TSLA):", "").upper()

if symbol:
    with st.spinner("Fetching data..."):
        df = fetch_history(symbol)
        metrics = calculate_metrics(df)

    st.subheader("Stock Summary")
    st.write(f"**Average Close Price:** ${metrics['Average Close Price']}")
    st.write(f"**Volatility:** {metrics['Volatility']}%")

    st.subheader("Price Trend")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Close'], label=f"{symbol} Close Price", color="blue")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    st.pyplot(fig)
