import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temprature')


if __name__ == '__main__':
    col = ['city', 'month', 'temprature']
    data = [
        ['jacksonVille', 'January', 13],
        ['jacksonVille', 'February', 23],
        ['jacksonVille', 'March', 38],
        ['jacksonVille', 'April', 5],
        ['jacksonVille', 'May', 34],
        ['Elpase', 'January', 20],
        ['Elpase', 'February', 6],
        ['Elpase', 'March', 26],
        ['Elpase', 'April', 2],
        ['Elpase', 'May', 43],
    ]
    pivot = pivotTable(pd.DataFrame(data, columns=col))
    print(pivot)
