import pandas as pd


def renameColumns(employees: pd.DataFrame) -> pd.DataFrame:
    employees.columns = ['student_id',
                         'first_name', 'last_name', 'age_in_years']
    return employees


if __name__ == "__main__":
    col = ['id', 'first', 'last', 'age']
    data = [
        ["846", 'Mason', 'las', 'Forward'],
        ["749", 'fgh', 'amd', 'Winger'],
        ["452", 'bvn', 'intl', 'cv'],
        ["753", 'fds', 'min', 'bg'],
        ["456", 'gh', 'lsd', 'ert'],
        ["450", 'sdfg', 'som', 'erfe'],
    ]
    dt = renameColumns(pd.DataFrame(data, columns=col))
    print(dt)
