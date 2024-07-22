from typing import List
from collections import defaultdict

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height={heights[i]:names[i] for i in range(len(names))}
        # heights.sort()
        h=sorted(heights)
        h.reverse()
        return [name_height[i] for i in h]

if __name__=='__main__':
    s = Solution()
    print(s.sortPeople(["Mary","John","Emma"],[180,165,170]))