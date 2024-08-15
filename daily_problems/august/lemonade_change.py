from typing import List
from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change=defaultdict(int)
        for i,bill in enumerate(bills):
            if bill==5:
                change[bill]+=1
            else:
                if bill==10:
                    if change[5]:
                        change[5]-=1
                        change[10]+=1
                    else:
                        return False
                elif bill==20:
                    print(i,change)
                    if change[5] and change[10]:
                        change[5]-=1
                        change[10]-=1
                    elif change[5]>=3:
                        change[5]-=3
                    else:
                        return False
        return True


if __name__=="__main__":
    s = Solution()
    # bills = [5,5,10,10,20]
    # bills = [5,5,5,10,20]
    # bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
    bills = [5,5,5,5,20,20,5,5,5,5]
    print(s.lemonadeChange(bills)) 