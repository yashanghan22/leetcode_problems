import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # ls = employees['salary'].to_list()
    # for i in range(len(ls)):
    #     ls[i] *= 2
    # employees.insert(loc=len(employees.columns), column='bonus',
    #                  value=ls, allow_duplicates=True)
    employees['bonus'] = employees['salary']*2
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
    bonus = createBonusColumn(pd.DataFrame(data, columns=col))
    print(bonus)
