from typing import List
import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    print(list(players.shape))
    return list(players.shape)


if __name__ == "__main__":
    col = ['player_id', 'name', 'age', 'position', 'team']
    data = [
        ["846", 'Mason', '21', 'Forward', 'RealMadrid'],
        ["749", 'fgh', '2', 'Winger', 'abad'],
        ["452", 'bvn', '67', 'cv', 'ads'],
        ["753", 'fds', '89', 'bg', 'ret'],
        ["456", 'gh', '34', 'ert', 'ert'],
        ["450", 'sdfg', 'dfg', 'erfe', 'cxvn'],
        ["452", 'bvn', '67', 'cv', 'ads'],
        ["753", 'fds', '89', 'bg', 'ret'],
        ["456", 'gh', '34', 'ert', 'ert'],
        ["450", 'sdfg', 'dfg', 'erfe', 'cxvn'],
    ]
    dt = getDataframeSize(pd.DataFrame(data, columns=col))
