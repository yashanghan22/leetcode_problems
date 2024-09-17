from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def helper(time: str) -> int:
            spt = time.split(':')
            hr = int(spt[0])
            mn = int(spt[1])
            return hr * 60 + mn
    
        min_list = [helper(time) for time in timePoints]
        
        min_list.sort()
        
        res = float('inf')
        
        for i in range(1, len(min_list)):
            res = min(res, min_list[i] - min_list[i - 1])
        
        circular_diff = 1440 + min_list[0] - min_list[-1]
        res = min(res, circular_diff)
        
        return res


if __name__=='__main__':
    s = Solution()
    print(s.findMinDifference(["23:59","00:00"]))