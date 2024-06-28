import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == '753']


if __name__ == "__main__":
    col = ['student_id', 'name', 'age']
    data = [
        ["846", 'Mason', '21'],
        ["749", 'fgh', '2'],
        ["452", 'bvn', '67'],
        ["753", 'fds', '89'],
        ["456", 'gh', '34'],
        ["450", 'sdfg', 'dfg'],
    ]
    dt = selectData(pd.DataFrame(data, columns=col))
    print(dt)
