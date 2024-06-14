from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l = 0
        r = len(costs)-1
        cost = 0
        while k > 0:
            a = min(tuple(costs[:candidates]))
            costs.remove(a)
            # print(costs[:candidates])
            cost += a
            # print(a)
            k -= 1
        return cost


if __name__ == '__main__':
    solution = Solution()
    # total = solution.totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4)
    total = solution.totalCost([1, 2, 4, 1], 3, 3)
    print(total)
