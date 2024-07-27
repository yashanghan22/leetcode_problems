from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj=defaultdict(list)

        for src , dst , cur_cost in zip(original,changed,cost):
            adj[src].append((dst,cur_cost))

        def dijkstra(src):
            heap=[(0,src)]
            min_cost_map={}
            
            while heap:
                cost,node=heapq.heappop(heap)
                if node in min_cost_map:
                    continue
                min_cost_map[node]=cost
                for nei, nei_cost in adj[node]:
                    heapq.heappush(heap,(cost+nei_cost,nei))
            print(src,min_cost_map)
            return min_cost_map
        min_cost_maps={c:dijkstra(c) for c in set(source)}
        res=0
        for src,dst in zip(source,target):
            if dst not in min_cost_maps[src]:
                return -1
            res+=min_cost_maps[src][dst]
        return res

if __name__=='__main__':
    s = Solution()
    print(s.minimumCost("abcd", "acbe", ["a","b","c","c","e","d"],["b","c","b","e","b","e"],[2,5,5,1,2,20]))