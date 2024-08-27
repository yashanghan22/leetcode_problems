from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        res=defaultdict(list)
        mx=0
        for (i,j),k in zip(edges,succProb):
            # print(i,j)
            res[i].append([j,k])
            res[j].append([i,k])
            # res[i][j]=k
            # res[j][i]=k
        # print(res)
        pq=[(-1,start_node)]
        visit=set()
        while pq:
            prob,cur=heapq.heappop(pq)
            visit.add(cur)
            if cur==end_node:
                return prob*-1
            for nei,edgeProb in res[cur]:
                if nei not in visit:
                    heapq.heappush(pq,(prob*edgeProb,nei))
        return 0

if __name__=="__main__":
    s = Solution()
    # print(s.maxProbability(3,[[0,1]],[0.5],0,2))
    # print(s.maxProbability(3,[[0,1],[1,2],[0,2]],[0.5,0.5,0.3],0,2))
    print(s.maxProbability(5,[[2,3],[1,2],[3,4],[1,3],[1,4],[0,1],[2,4],[0,4],[0,2]],[0.06,0.26,0.49,0.25,0.2,0.64,0.23,0.21,0.77],0,3))