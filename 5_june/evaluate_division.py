from typing import List
from collections import defaultdict


class Solution:
    # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    #     graph = defaultdict(dict)

    #     for (u, v), val in zip(equations, values):
    #         graph[u][u] = graph[v][v] = 1
    #         graph[u][v] = val
    #         graph[v][u] = 1 / val
    #         # print(u, v, val)

    #     print(graph)
    #     for k in graph:
    #         # ---5
    #         # print(k)
    #         for i in graph[k]:
    #             # ---2-3----
    #             for j in graph[k]:
    #                 # print(str(i) + str(j) +
    #                 #       str(graph[i][j]) + str(graph[i][k]) + str(graph[k][j]))
    #                 graph[i][j] = graph[i][k] * graph[k][j]
    #     print(graph)
    #     for u, v in queries:
    #         print(graph[u].get(v, -1))
    #     return [graph[u].get(v, -1) for u, v in queries]
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        formula = defaultdict(dict)
        count = 1
        lst=[float]
        for (l, r), val in zip(equations, values):
            formula[l][l] = formula[r][r] = 1
            formula[l][r] = val
            formula[r][l] = 1/val
        print(formula)
        for f in formula:
            for i in formula[f]:
                # print('=====')
                for j in formula[f]:
                    count += 1
                    # print(f+' '+i+' '+j)
                    # print(formula[i][f], formula[f][j])
                    formula[i][j] = formula[i][f]*formula[f][j]
                    # print(formula[i][j])
                    # print(formula[f][j])
        # print(count)
        # print(formula)
        # for a,b in queries:
        #     c=formula[a][a]/formula[a][b]
        #     print(formula[b][a],formula[a][b])
        for a,b in queries:
            lst.append(formula[a][b])
        return lst


if __name__ == '__main__':
    solution = Solution()
    val = solution.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
                                [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]])
    # val = solution.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [
    #                             ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    print(val)
