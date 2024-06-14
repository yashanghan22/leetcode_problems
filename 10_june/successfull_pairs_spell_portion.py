from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        lst = []
        for i in range(len(spells)):
            l = []
            count = 0
            for j in range(len(potions)):
                c = spells[i]*potions[j]
                l.append(c)
                if c >= success:
                    count += 1
            lst.append(count)
        return lst


if __name__ == '__main__':
    solution = Solution()
    # pair = solution.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)
    pair = solution.successfulPairs([3, 1, 2], [8, 5, 8], 16)
    print(pair)
