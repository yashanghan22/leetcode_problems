import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary']*2
    return employees


if __name__ == '__main__':
    col = ['name', 'salary']
    data = [
        ['piper', 4548],
        ['Grace', 28150],
        ['Georgia', 1103],
        ['willow', 6593],
        ['Finn', 74576],
    ]
    bonus = modifySalaryColumn(pd.DataFrame(data, columns=col))
    print(bonus)
