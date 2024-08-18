class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res=[1]
        i2,i3,i5=0,0,0
        for i in range(1,n):
            next_num=min(res[i2]*2,res[i3]*3,res[i5]*5)
            res.append(next_num)
            if next_num==res[i2]*2:
                i2+=1
            if next_num==res[i3]*3:
                i3+=1
            if next_num==res[i5]*5:
                i5+=1
        return res[n-1]


if __name__=='__main__':
    s = Solution()
    print(s.nthUglyNumber(10))  # 12