import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers = customers[customers['id'] != 3]['name']
    customers.columns = [
        'Customers'
    ]
    return customers


if __name__ == '__main__':
    col1 = ['id', 'name']
    data1 = [
        [1, 'Joe'],
        [2, 'Henry'],
        [3, 'Sam'],
        [4, 'Max'],
    ]
    col2 = ['id', 'customerId']
    data2 = [
        [1, 3],
        [2, 1],
    ]
    fnd = find_customers(pd.DataFrame(data1, columns=col1),
                         pd.DataFrame(data2, columns=col2))
    print(fnd)
