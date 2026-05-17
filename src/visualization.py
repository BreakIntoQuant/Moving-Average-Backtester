import matplotlib.pyplot as plt


def plot_strategy(data, ticker):

    plt.figure(figsize=(14, 7))

    plt.plot(
        data['Cumulative Market Return'],
        label='Buy and Hold'
    )

    plt.plot(
        data['Cumulative Strategy Return'],
        label='MA Strategy'
    )

    plt.title(
        f'{ticker} Moving Average Strategy'
    )

    plt.xlabel('Date')
    plt.ylabel('Portfolio Growth')

    plt.legend()

    plt.grid(True)

    plt.savefig(
        f'charts/{ticker}_strategy.png'
    )

    print("Chart saved.")