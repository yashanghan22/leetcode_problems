from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = len(isConnected)
        checkedIndex = set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                # if isConnected[i][j] == isConnected[j][i]:
                #     print('i and j', i, j)
                if i != j and isConnected[j][i] == 1:
                    # print('i and j', i, j)
                    if i and j not in checkedIndex:
                        count -= 1
                        checkedIndex.update([i, j])
        return count


if __name__ == '__main__':
    solution = Solution()
    # val = solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    # val = solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    val = solution.findCircleNum([[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]])
    print('solution of find cicleNum:', val)
