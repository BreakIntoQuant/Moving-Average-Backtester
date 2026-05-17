from data_loader import fetch_stock_data
from strategy import create_signals
from backtester import backtest_strategy
from visualization import plot_strategy


def main():

    ticker = "AAPL"

    data = fetch_stock_data(
        ticker,
        "2020-01-01",
        "2025-01-01"
    )

    data = create_signals(data)

    data = backtest_strategy(data)

    print(data.head())

    plot_strategy(data, ticker)

    print("\nBacktest complete.")


if __name__ == "__main__":
    main()