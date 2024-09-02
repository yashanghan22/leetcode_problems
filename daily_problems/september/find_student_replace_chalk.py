from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk

        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]

if __name__=='__main__':
    chalk = [3,4,1,2]
    k = 25
    print(Solution().chalkReplacer(chalk, k))  # Output: 2