from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res=0
        for log in logs:
            if log == "../":
                res=max(0,res-1)
            elif log=='./':
                continue
            else:
                res += 1
        return res


if __name__=='__main__':
    s = Solution()
    print(s.minOperations(["d1/","d2/","../","d21/","./"]))
    print(s.minOperations(["d1/","../","../","../"]))