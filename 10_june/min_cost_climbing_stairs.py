from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = 0
        if len(cost) < 4:
            return min(cost) if len(cost) == 2 else cost[1]
        p = 0
        if cost[0] > cost[1]:
            p = 1
            total += cost[p]
        else:
            total += cost[p]

        while p < (len(cost)-2):
            if cost[p+1] > cost[p+2] or cost[p+1] == cost[p+2]:
                p += 2
                total += cost[p]
            elif cost[p+1] < cost[p+2]:
                p += 1
                total += cost[p]
            # p += 1
            # if cost[p+1] == cost[p+2]:
            #     p += 2
            #     total += cost[p]

        return total


if __name__ == '__main__':
    solution = Solution()
    # minCost = solution.minCostClimbingStairs([10, 15, 20])
    minCost = solution.minCostClimbingStairs(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(minCost)
