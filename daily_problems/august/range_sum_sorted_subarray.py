from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        total=0
        subArray=[]
        for i in range(len(nums)):
            subArray.append(nums[i]+total)
            total+=nums[i]
        subArray1=[]
        for j in range(len(subArray)):
            for k in range(j,len(subArray)):
                if j!=k:
                    subArray1.append(subArray[k]-subArray[j])
                    # print(subArray[j],subArray[k])
        subArray+=subArray1
        subArray.sort()
        res=0
        for m in range(len(subArray)):
            print(m)
            if m+1>=left and m+1<=right:
                res+=subArray[m]
        return res%(pow(10,9)+7)


if __name__=="__main__":
    s = Solution()
    print(s.rangeSum([1,2,3,4],4,1,5))