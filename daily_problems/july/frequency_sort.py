from typing import List
from collections import defaultdict,OrderedDict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq=defaultdict(int)
        res=[]
        for i in nums:
            freq[i]+=1
        print(freq)
        print(list(freq.keys()))
        sort=sorted(freq.items(),key=lambda X:(X[1],-X[0]))
        print(sort)
        for k,v in sort:
            print(k,[k]*v)
            res+=[k]*v
        return res


if __name__=='__main__':
    # nums = [1,1,2,2,2,3]
    # nums = [2,3,1,3,2]
    nums = [-1,1,-6,4,5,-6,1,4,1]
    print(Solution().frequencySort(nums))