from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res=[]
        if len(original)!=m*n:
            return []
        i=0
        lst=[]
        while i<len(original):
            lst.append(original[i])
            print(lst)
            if (i+1)%n==0:
                print(i,lst)
                res.append(lst)
                # i+=(n-1)
                lst=[]
                # continue
            i+=1
        return res

if __name__=='__main__':
    s = Solution()
    print(s.construct2DArray([1,2,3,4,5,6], 3, 2))