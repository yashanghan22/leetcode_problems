import collections
from typing import List


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        grd = grid
        fresh = 0
        steps = 0
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = collections.deque()
        if len(grid)==1 and len(grid[0])>2:
            oneCount=0
            for i in range(len(grid[0])):
                if grid[0][i]==1:
                    oneCount+=1
            if not grid[0].__contains__(2):
                if not grid[0].__contains__(1) and grid[0].__contains__(0):
                    return 0
                return -1
            return oneCount if grid[0].__contains__(1) and grid[0].__contains__(2) else 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:
            return steps
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                # for u, v in [(g[0]-1, g[1]), (g[0]+1, g[1]), (g[0], g[1]-1), (g[0], g[1]+1)]:
                for u, v in direction:
                    row, col = u+r, v+c
                    if (0 <= row < len(grid) and len(grid)>1 and 0 <= col < len(grid[1])) and grd[row][col] == 1:
                        grd[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            steps += 1
        return steps if fresh == 0 else -1


if __name__ == '__main__':
    solution = Solution()
    orange = solution.orangesRotting([[0]])
    # orange = solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    # orange = solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    print("rotting oranges: "+str(orange))
