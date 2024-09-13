from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0] * len(arr)
        prefix_xor[0] = arr[0]
        
        for i in range(1, len(arr)):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]
        
        res = []
        for q in queries:
            L, R = q
            if L == 0:
                res.append(prefix_xor[R])
            else:
                res.append(prefix_xor[R] ^ prefix_xor[L - 1])
        
        return res


if __name__=='__main__':
    s = Solution()
    # print(s.xorQueries( [1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))
    print(s.xorQueries( [4,8,2,10],[[2,3],[1,3],[0,0],[0,3]]))