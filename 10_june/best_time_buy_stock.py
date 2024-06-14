from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ma = defaultdict(list)
        maxProfit = [0 for _ in range(len(prices))]
        for i in prices:
            for j in prices:
                st = (j-i)-fee
                # ma[i][j] = st if st > 1 else 0
                ma[i] = ma[i]+[st if st > 1 else 0]
                # if st > 1:
                #     print(st)
                #     ma[i][j] = st
        for k in ma:
            for l in range(len(maxProfit)):
                maxProfit[l] = max(maxProfit[l], ma[k][l])

        print(ma)
        print(maxProfit)
        return 0


if __name__ == '__main__':
    solution = Solution()
    # maxP = solution.maxProfit([1, 3, 2, 8, 4, 9], 2)
    maxP = solution.maxProfit([1, 3, 7, 5, 10, 3], 3)
