class Solution:
    def findComplement(self, num: int) -> int:
        bn=list("{0:b}".format(num))
        for i in range(len(bn)):
            if bn[i]=='0':
                bn[i]='1'
            elif bn[i]=='1':
                bn[i]='0'
        return int(''.join(bn),2)

if __name__=='__main__':
    s = Solution()
    print(s.findComplement(5))