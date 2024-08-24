class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if n == "1":
            return "0"
        if n == "0":
            return "1"

        first_half = n[:(length + 1) // 2]
        candidates = set()
       
        candidates.add(int(first_half + first_half[:-1][::-1]))
        candidates.add(int(first_half + first_half[::-1]))
        
        
        for change in [-1, 1]:
            new_first_half = str(int(first_half) + change)
            candidates.add(int(new_first_half + new_first_half[:-1][::-1]))
            candidates.add(int(new_first_half + new_first_half[::-1]))

       
        candidates.add(10**(length-1) - 1)
        candidates.add(10**length + 1)
        candidates.discard(int(n))
        
        return str(min(candidates, key=lambda x: (abs(x - int(n)), x)))
        # k=int(n)
        # # if k<100:
        # #     # return str(max(0,k-1,k+1,k+9,k-9))
        # #     return str(max(0,k-1))
        # # res=0
        # def backward(b:int)-> int:
        #     if not b:
        #         return 0
        #     print(b)
        #     if str(b)==str(b)[::-1]:
        #         return int(str(b)[::-1])
        #     b-=1
        #     return backward(b)
        # def forward(f:int)->int:
        #     if not f:
        #         return 0
        #     if str(f)==str(f)[::-1]:
        #         return int(str(f)[::-1])
        #     f+=1
        #     return forward(f)
        # bw=backward(k-1)
        # fw=forward(k+1)
        # closet=(k-bw)<=(fw-k)
        # print(closet)
        # # res=min(backword(k-1),forward(k+1))
        # return str(bw if closet else fw)


if __name__=='__main__':
    s = Solution()
    # print(s.nearestPalindromic('807045053224792883'))
    print(s.nearestPalindromic('1213'))
    # print(s.nearestPalindromic('1'))
    # print(s.nearestPalindromic('123'))