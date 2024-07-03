import heapq

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        
        minF=sorted(heapq.nsmallest(4,nums))
        maxF=sorted(heapq.nlargest(4,nums))
        res=float('inf')

        for i in range(4):
            res=min(res,maxF[i]-minF[i])
        return res


if __name__=='__main__':

    nums=[1,5,0,10,14]

    solution=Solution().minDifference(nums=nums)
    print(solution)