import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.melt(id_vars='product', var_name='quarter', value_name='sales')


if __name__ == '__main__':
    col = ['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4']
    data = [
        ['Umbrella', 417, 224, 379, 611],
        ['SleepingBag', 564, 456, 329, 311],
    ]
    pivot = pivotTable(pd.DataFrame(data, columns=col))
    print(pivot)
