from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj=defaultdict(list)
        for v1,v2, dist in edges:
            adj[v1].append((v2,dist))
            adj[v2].append((v1,dist))
        
        def dijkstra(src):
            heap=[(0,src)]
            visit=set()
            
            while heap:
                dist,node=heapq.heappop(heap)
                print(dist,node)
                if node in visit:
                    continue
                visit.add(node)
                for nei,dis in adj[node]:
                    nei_dist=dist+dis
                    if nei_dist <=distanceThreshold:
                        heapq.heappush(heap,(nei_dist,nei))
            return len(visit)-1
        
        res,min_count=-1,n
        for src in range(n):
            count=dijkstra(src)
            if count <=min_count:
                res,min_count=src,count
        print(adj)
        return res


if __name__=='__main__':
    s = Solution()
    print(s.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))