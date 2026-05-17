def backtest_strategy(data):

    data['Market Return'] = (
        data['Close']
        .pct_change()
    )

    data['Strategy Return'] = (
        data['Market Return']
        * data['Signal'].shift(1)
    )

    data['Cumulative Market Return'] = (
        1 + data['Market Return']
    ).cumprod()

    data['Cumulative Strategy Return'] = (
        1 + data['Strategy Return']
    ).cumprod()

    return data