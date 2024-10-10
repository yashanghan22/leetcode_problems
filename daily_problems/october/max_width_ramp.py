from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                res = max(res, j - stack.pop())
        
        return res


if __name__=='__main__':
    s = Solution()
    print(s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))
    # print(s.maxWidthRamp([6,0,8,2,1,5]))