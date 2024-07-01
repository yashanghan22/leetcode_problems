from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l=0
        m=1
        r=2
        while r<len(arr):
            if arr[l]%2==1 and arr[m]%2==1 and arr[r]%2==1:
                return True
            # if not arr[l]%2==1 or not arr[r]%2==1:
            #     count=0
            r+=1
            l+=1
            m+=1
        return False


if __name__=='__main__':
    solution=Solution()
    # print(solution.threeConsecutiveOdds([2,6,4,1]))
    print(solution.threeConsecutiveOdds([1,1,2,1,1]))
    # print(solution.threeConsecutiveOdds([1,1,1]))
    print(solution.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))