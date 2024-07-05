import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])


if __name__ == '__main__':
    col = ['student_id', 'name', 'age']
    data1 = [
        [1, 'Mason', 8],
        [2, 'Ava', 6],
        [3, 'taylor', 8],
        [4, 'Georgia', 25],
    ]
    data2 = [
        [7, 'tayl', 2],
        [8, 'Jack', 7],
    ]
    con = concatenateTables(pd.DataFrame(
        data=data1, columns=col), pd.DataFrame(data=data2, columns=col))
    print(col)
