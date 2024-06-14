from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        leftT = set()
        rightN = set()
        count = 0
        towordZero = {}
        for i in connections:
            print('-=>', i[0], i[1])
            towordZero[i[0]] = i[1]
            if i[0] == 0:
                rightN.add(i[1])
            if i[1] == 0:
                leftT.add(i[0])
            if leftT.__contains__(i[0]):
                count += 1
                rightN.add(i[1])
            if rightN.__contains__(i[0]):
                count += 1
        print(leftT)
        print(rightN)
        return 0 if len(rightN) == 1 and rightN.__contains__(0) else count


if __name__ == '__main__':
    solution = Solution()
    lst = [[1, 0], [2, 0]]
    # lst = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    # lst = [[1, 0], [1, 2], [3, 2], [3, 4]]
    out = solution.minReorder(8, lst)
    print('out solution:', out)
