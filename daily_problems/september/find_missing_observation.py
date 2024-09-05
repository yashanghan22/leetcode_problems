from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n)
        sum_rolls = total - sum(rolls)

        if sum_rolls < n or sum_rolls > 6 * n:
            return []

        base_roll = sum_rolls // n
        remainder = sum_rolls % n
        res = [base_roll + 1] * remainder + [base_roll] * (n - remainder)
        return res
        # total =   mean * (len(rolls)+n)
        # sum_rolls = total- sum(rolls)
        # res=[]
        # for i in range(n):
        #     min_roll=min(6,sum_rolls-(n-i)+1)
        #     res.append(min_roll)
        #     sum_rolls -= min_roll
        # if sum(rolls+res)/(len(rolls)+n)==mean:
        #     return res
        # return []

if __name__=='__main__':
    s = Solution()
    print(s.missingRolls([3,2,4,3],4,2))