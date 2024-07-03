import pandas as pd


def dropMissingData(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop(customers[customers['name'].isnull()].index)


if __name__ == '__main__':
    col = ['student_id', 'name', 'age']
    data = [
        ["846", 'Mason', '21'],
        ["749", None, '2'],
        ["452", 'bvn', '67'],
        ["753", None, '89'],
        ["456", 'gh', '34'],
        ["450", 'sdfg', 'dfg'],
    ]
    bonus = dropMissingData(pd.DataFrame(data, columns=col))
    print(bonus)
