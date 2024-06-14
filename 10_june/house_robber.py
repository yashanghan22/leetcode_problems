from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        odd = []
        even = []
        for i in range(len(nums)):
            # if i == 0:
            #     odd.append(nums[i])
            if (i+1) % 2 == 0:
                even.append(nums[i])
            if (i+1) % 2 != 0:
                odd.append(nums[i])
            # else:
            #     odd.append(nums[i])
        # print(odd)
        # print(even)
        return max(sum(odd), sum(even))


if __name__ == '__main__':
    solution = Solution()
    rob = solution.rob([2, 7, 9, 3, 1])
    # rob = solution.rob([1, 2, 3, 1])
    print(rob)
