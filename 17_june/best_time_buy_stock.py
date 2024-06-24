from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ma = defaultdict(list)
        maxProfit = [0 for _ in range(len(prices))]
        mn = 0
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                mn = prices[i]
            else:
                pf = prices[i]-mn-fee
                # print(mn, mx, pf, profit)
                profit = max(profit, pf)
                mn = min(mn, prices[i]-profit)
        print(profit)
        return profit


if __name__ == '__main__':
    solution = Solution()
    # maxP = solution.maxProfit([1, 3, 2, 8, 4, 9], 2)
    maxP = solution.maxProfit([1, 3, 7, 5, 10, 3], 3)
