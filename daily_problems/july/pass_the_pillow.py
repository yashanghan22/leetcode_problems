class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        rev=False
        while time>0:
            time-=1
            if rev:
                i-=1
            else:
                i+=1
            if i==n:
                rev=True
            if i==1:
                rev=False
        return i


if __name__=='__main__':
    s = Solution()
    print(s.passThePillow(4,7))
    print(s.passThePillow(3,2))