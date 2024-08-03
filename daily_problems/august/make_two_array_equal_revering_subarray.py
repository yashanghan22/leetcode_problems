from typing import List
from collections import defaultdict

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic=defaultdict(int)
        for i,j in zip(target,arr):
            dic[j]+=1
            dic[i]-=1
        for k,v in dic.items():
            if v!=0:
                return False
        return True 
        # return sorted(target) == sorted(arr)

if __name__=="__main__":
    s = Solution()
    print(s.canBeEqual([1,2,3,4],[2,4,1,3]))