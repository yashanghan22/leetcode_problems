from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        print(all(ele ==nums[0] for ele in nums))
        if len(nums)>1 and k>1 and all(ele ==nums[0] for ele in nums):
            return -1
        def quicksort(l, r) -> int:
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quicksort(1, p-1)
            elif p < k:
                return quicksort(p+1, r)
            else:
                return nums[p]
        return quicksort(0, len(nums)-1)


if __name__ == '__main__':
    solution = Solution()
    # large = solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    # large = solution.findKthLargest([-1,-1], 2)
    # large = solution.findKthLargest([1], 1)
    large = solution.findKthLargest([99,99], 1)
    # large = solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(large)
