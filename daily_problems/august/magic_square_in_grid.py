from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        def magic(r,c):
            values=set()

            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] in values or not (1<=grid[i][j]<=9):
                        return 0
                    values.add(grid[i][j])
            for i in range(r,r+3):
                if sum(grid[i][c:c+3])!=15:
                    return 0
            for i in range(c,c+3):
                if (grid[r][i]+ grid[r+1][i]+grid[r+2][i])!=15:
                    return 0
            if (grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2])!=15 or (grid[r][c+2]+grid[r+1][c+1]+grid[r+2][c])!=15:
                return 0
            return 1
        count=0
        for r in range(row-2):
            for c in range(col-2):
                count+=magic(r,c)
        return count

if __name__=='__main__':
    s=Solution()
    print(s.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))