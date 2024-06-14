from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = 0
        for i in range(len(nums)):
            print(nums[i], i)
            if i != 0 and i < len(nums) and (nums[i-1] < nums[i] > nums[i+1]) and peak < nums[i]:
                peak = i
        return peak


if __name__ == '__main__':
    solution = Solution()
    # peakIndex = solution.findPeakElement([1, 2, 3, 1])
    peakIndex = solution.findPeakElement([1, 2, 1, 3, 5, 6, 4])
    print(peakIndex)
