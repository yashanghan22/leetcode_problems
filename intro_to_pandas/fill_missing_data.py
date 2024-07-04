import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(inplace=None, value=0)
    return products


if __name__ == "__main__":
    col = ['name', 'quantity', 'price']
    data = [
        ['Mason', 21, 73.0],
        ['fgh', None, 12.5],
        ['bvn', 67, 6.5],
        ['fds', None, 23.14],
        ['gh', 34, 23.7],
        ['sdfg', 5, 45.5],
    ]
    dt = fillMissingValues(pd.DataFrame(data, columns=col))
    print(dt)
