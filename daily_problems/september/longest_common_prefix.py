from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1)>len(arr2):
            arr1,arr2=arr2,arr1
        prefix_set=set()
        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n=n//10
        res=0
        for n in arr2:
            while n and n not in prefix_set:
                n=n//10
            if n:
                res=max(res,len(str(n)))
        return res
        # res=''
        # for i in set(arr2):
        #     for j in set(arr1):
        #         if str(i).find(str(j))==0:
        #             if len(res)<len(str(j)):
        #                 res=str(j)
        # return len(res)


if __name__=='__main__':
    s = Solution()
    # print(s.longestCommonPrefix([1,10,100],[1000]))
    print(s.longestCommonPrefix([1,2,3],[4,4,4]))