from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        for m in range(1,len(rating)-1):
            left_smaller=right_larger=0
            for i in range(m):
                if rating[i]<rating[m]:
                    left_smaller+=1
            for i in range(m+1,len(rating)):
                if rating[i]>rating[m]:
                    right_larger+=1
            count+=left_smaller*right_larger

            left_larger=m-left_smaller
            right_smaller=len(rating)-m-1-right_larger
            count+=left_larger*right_smaller
        return count

if __name__=='__main__':
    s=Solution()
    print(s.numTeams([3,6,7,5,1]))
    print(s.numTeams([4,7,9,5,10,8,2,1,6]))
    print(s.numTeams([2,5,3,4,1]))