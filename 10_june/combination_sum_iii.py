from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(start: int, path: List[int], currSum: int):
            print(path)
            if len(path) == k and currSum == n:
                res.append(path)
                return
            elif (len(path) == k and currSum != n):
                return
            # Will always starts on a number that hasn't been used before,
            # So don't need to record what number has been visited
            for i in range(start, 10):
                dfs(i+1, path+[i], currSum+i)

        dfs(1, [], 0)
        return res
        # -------------can be used for when k is 3 ------------
        # len = k+1
        # for i in range(1, len):
        #     for j in range(1, 9):
        #         for l in range(1, 9):
        #             if i+j+l == n and i != j and j != l and i != l:
        #                 sm = [i, j, l]
        #                 sm.sort()
        #                 if not res.__contains__(sm):
        #                     res.append(sm)
        #                     print(i, j, l)
        # return res


if __name__ == '__main__':
    solution = Solution()
    combination = solution.combinationSum3(3, 7)
    combination = solution.combinationSum3(3, 9)
    # combination = solution.combinationSum3(4, 13)
    # combination = solution.combinationSum3(2, 3)
    # print(combination)
