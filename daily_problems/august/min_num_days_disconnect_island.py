from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        def dfs(r,c,visit):
            # print(visit)
            if (r<0 or c<0 or r==row or c==col or grid[r][c]==0 or (r,c)  in visit):
                return
            visit.add((r,c))
            neighbors=[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            for nr,nc in neighbors:
                dfs(nr,nc,visit)
        def count_islands():
            visit=set()
            count=0
            for r in range(row):
                for c in range(col):
                    if grid[r][c] and (r,c) not in visit:
                        dfs(r,c,visit)
                        # print(r,c,visit)
                        count+=1
            return count
        if count_islands()!=1:
            return 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    continue
                grid[r][c]=0
                if count_islands()!=1:
                    return 1
                grid[r][c]=1
        return 2

if __name__=='__main__':
    s=Solution()
    print(s.minDays([[1,1]]))
    print(s.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))