from typing import List
import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_names = ['student_id', 'age']
    return pd.DataFrame(student_data, columns=column_names)


if __name__ == '__main__':
    v = createDataframe([
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ])
    print(v)
