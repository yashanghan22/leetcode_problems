from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        mp={}
        total=0
        for i in roads:
            if not i[0] in mp:
                mp[i[0]]=1
            if not i[1] in mp:
                mp[i[1]]=1
            mp[i[0]]+=1
            mp[i[1]]+=1
        count=0
        lt=sorted(mp.items(),key=lambda x:x[1])
        lt.reverse()
        for k,v in lt:
            mp[k]=n-count
            print(mp[k])
            count+=1
        for i in roads:
            total+=mp[i[0]]+mp[i[1]]
        print(total)
        return total


if __name__=='__main__':
    solution=Solution()
    # mx=solution.maximumImportance(5,[[0,1]])
    mx=solution.maximumImportance(5,[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])