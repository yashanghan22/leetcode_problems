import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df=world[(world['area'] >= 3000000) & (world['population'] >= 25000000)]
    return df


if __name__ == '__main__':
    col = ['name', 'continent', 'area', 'population', 'gdp']
    data = [
        ['Afghanistan', 'Asia', 6522000, 25510000, 30343020230],
        ['Albenia', 'Europe', 6520, 25456500, 30343020230],
        ['Argeria', 'Africa', 8262000, 25100, 30343020230],
        ['Andorra', 'Europe', 250, 27400, 30343020230],
        ['Angola', 'Africa', 7890600, 25422100, 30343020230],
    ]
    big = big_countries(pd.DataFrame(data, columns=col))
    print(big)
