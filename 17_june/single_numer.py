from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for r in nums:
            res = r ^ res
        return res


if __name__ == '__main__':
    solution = Solution()
    single = solution.singleNumber([4, 1, 2, 1, 2])
    print(single)
