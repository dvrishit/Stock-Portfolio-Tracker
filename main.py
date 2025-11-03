import matplotlib.pyplot as plt
from data_fetch import fetch_history
from analytics import calculate_metrics

def visualise(df, symbol):
    plt.figure(figsize=(10,5))
    plt.plot(df['Close'], label=f'{symbol} Close Price', linewidth=2)
    plt.title(f'{symbol} Stock Price History')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    df = fetch_history(symbol)
    metrics = calculate_metrics(df)
    print("\nStock Summary:")
    for key, value in metrics.items():
        print(f"{key}: {value}")


    visualise(df, symbol)

if __name__ == "__main__":
    main()

    