import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[:2]


if __name__ == "__main__":
    col = ['employee_id', 'name', 'department', 'salary']
    data = [
        ["846", 'Mason', '21', 'Forward'],
        ["749", 'fgh', '2', 'Winger'],
        ["452", 'bvn', '67', 'cv'],
        ["753", 'fds', '89', 'bg'],
        ["456", 'gh', '34', 'ert'],
        ["450", 'sdfg', 'dfg', 'erfe'],
    ]
    dt = selectFirstRows(pd.DataFrame(data, columns=col))
    print(dt)
