import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df=animals.sort_values(by=['weight'],ascending=False)
    df=df.loc[df['weight']>100,['name']]
    return df


if __name__ == '__main__':
    col = ['name', 'specials', 'age', 'weight']
    data = [
        ['Tatiana', 'Snake', 98, 464],
        ['Khaled', 'Giraffe', 23, 42],
        ['Alex', 'Leopard', 42, 463],
        ['Jonathan', 'Monkey', 75, 280],
        ['Stephen', 'Bear', 56, 50],
        ['Tommy', 'Panda', 21, 123],
    ]
    fnd = findHeavyAnimals(pd.DataFrame(data, columns=col))
    print(fnd)
