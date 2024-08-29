from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(stones)):
                if j not in visited and (stones[j][0] == stones[i][0] or stones[j][1] == stones[i][1]):
                    visited.add(j)
                    dfs(j)
        visited=set()
        removed_stone=0
        for i in range(len(stones)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                removed_stone+=1
        return len(stones)- removed_stone


if __name__=='__main__':
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(Solution().removeStones(stones))