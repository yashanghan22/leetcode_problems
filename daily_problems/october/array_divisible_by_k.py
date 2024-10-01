from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        if remainder_count[0] % 2 != 0: 
            return False
        
        for i in range(1, k):
            if remainder_count[i] != remainder_count[k - i]: 
                return False
        return True


if __name__=='__main__':
    s=Solution()
    print(s.canArrange([1,2,3,4,5,10,6,7,8,9],10))