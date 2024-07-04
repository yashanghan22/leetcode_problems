import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    print(students)
    students['grade'] = students['grade'].astype(dtype=int)
    # students['grade'].astype(dtype=int)
    return students


if __name__ == "__main__":
    col = ['student_id', 'name', 'age', 'grade']
    data = [
        ["846", 'Mason', 21, 73.0],
        ["749", 'fgh', 2, 12.5],
        ["452", 'bvn', 67, 56.2],
        ["753", 'fds', 89, 23.14],
        ["456", 'gh', 34, 23.7],
        ["450", 'sdfg', 5, 45.5],
    ]
    dt = changeDatatype(pd.DataFrame(data, columns=col))
    print(dt)
