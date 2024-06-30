from typing import List

from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # direct_child = defaultdict(list)
        # ans = [[] for _ in range(n)]
        # for x, y in edges:
        #     direct_child[x].append(y)
        # print(direct_child)
        # def dfs(x, curr):
        #     for ch in direct_child[curr]:
        #         if ans[ch] and ans[ch][-1] == x: continue
        #         ans[ch].append(x)
        #         dfs(x, ch) 
        
        # for i in range(n): dfs(i, i)
        # return ans
        lst=[[]]*n
        ancetor=defaultdict(list)
        for i in edges:
            if not ancetor.__contains__(i[0]):
                ancetor[i[0]]=[]

            var =ancetor[i[1]]
            if i[0] not in var:
                var.append(i[0])
            ancetor[i[1]]=var

        for j in range(n):
            for l in ancetor[j]:
                ls=set(lst[j]+ancetor[l]+ancetor[j])
                # print(j,lst[j],ancetor[l]+ancetor[j])
                lst[j]=list(ls)
                lst[j].sort()
                # lst[j]+=ancetor[l]

        print(ancetor)
        return lst


if __name__=='__main__':
    solution=Solution() 
    ancentor=solution.getAncestors(8,[[0,7],[7,6],[0,3],[6,3],[5,4],[1,5],[2,7],[3,5],[3,1],[0,5],[7,5],[2,1],[1,4],[6,1]])
    # ancentor=solution.getAncestors(8,[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])
    print(ancentor)