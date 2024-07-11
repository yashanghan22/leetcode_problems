from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,j in enumerate(nums):
            for k,l in enumerate(nums):
                if i!=k and j+l==target:
                    return [i,k]
        return [l,r]


if __name__=='__main__':
    s=Solution()
    # print(s.twoSum([2,7,11,15],9))
    print(s.twoSum([3,2,4],6))