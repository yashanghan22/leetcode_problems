import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]['product_id']


if __name__ == '__main__':
    col = ['product_id', 'low_fats', 'recyclable']
    data = [
        [0, 'Y', 'N'],
        [1, 'Y', 'N'],
        [2, 'Y', 'Y'],
        [3, 'Y', 'N'],
        [4, 'N', 'N'],
        [5, 'Y', 'Y'],
    ]
    fnd = find_products(pd.DataFrame(data, columns=col))
    print(fnd)
