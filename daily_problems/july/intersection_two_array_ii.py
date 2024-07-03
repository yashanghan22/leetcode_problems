from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls=[]
        count=defaultdict(int)
        for i in nums1:
            count[i]+=1
        for j in nums2:
            if  j in count.keys() and count[j]>=1:
                ls.append(j)
                count[j]-=1
        return ls
    

if __name__=="__main__":
    solution=Solution()
    print(solution.intersect([1,2,2,1],[2,2]))
    print(solution.intersect([4,9,5],[9,4,9,8,4]))