from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res=[]
        r,c=rStart,cStart
        step=1
        k=0
        while len(res)<rows*cols:
            for _ in range(2):
                dr,dc=directions[k]
                for _ in range(step):
                    if (0<=r<rows)and(0<=c<cols):
                        res.append([r,c])
                    r,c=r+dr,c+dc
                k=(k+1)%4
            step+=1
        return res

if __name__=='__main__':
    s=Solution()
    print(s.spiralMatrixIII(5, 6, 1, 4))