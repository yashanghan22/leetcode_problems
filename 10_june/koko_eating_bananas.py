import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = math.ceil(sum(piles)/h), max(piles)
        res = r
        while l <= r:
            k = l+(r-l)//2
            print(l, r)
            hour = 0
            for i in piles:
                hour += math.ceil(i/k)
            print(hour)
            if hour > h:
                l = k+1
            else:
                res = k
                r = k-1
        return res


if __name__ == '__main__':
    solution = Solution()
    # min = solution.minEatingSpeed([3, 6, 7, 11], 8)
    min = solution.minEatingSpeed([30, 11, 23, 4, 20], 6)
    print(min)
