from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
        def helper(n1,n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1
        nums=sorted(nums,key=cmp_to_key(helper))
        return str(int(''.join(nums)))


if __name__=='__main__':
    s=Solution()
    print(s.largestNumber([10,2]))