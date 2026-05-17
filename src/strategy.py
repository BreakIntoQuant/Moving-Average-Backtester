def create_signals(
    data,
    short_window=20,
    long_window=50
):

    data['SMA_Short'] = (
        data['Close']
        .rolling(window=short_window)
        .mean()
    )

    data['SMA_Long'] = (
        data['Close']
        .rolling(window=long_window)
        .mean()
    )

    data['Signal'] = 0

    data.loc[
        data['SMA_Short'] > data['SMA_Long'],
        'Signal'
    ] = 1

    data.loc[
        data['SMA_Short'] < data['SMA_Long'],
        'Signal'
    ] = -1

    return data