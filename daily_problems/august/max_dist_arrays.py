from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min,cur_max=arrays[0][0],arrays[0][-1]
        res=0
        for i in range(1,len(arrays)):
            r=arrays[i]
            res=max(res,r[-1]-cur_min,cur_max-r[0])
            cur_min=min(cur_min,r[0])
            cur_max=max(cur_max,r[-1])
        return res

if __name__=='__main__':
    s = Solution()
    print(s.maxDistance([[1,5],[3,4]]))