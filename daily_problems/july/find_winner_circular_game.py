class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner=0
        for i in range(1,n+1):
            winner=(winner+k)%i
            print(winner,i)
        return winner+1


if __name__=='__main__':
    s = Solution()
    # print(s.findTheWinner(5,2))
    print(s.findTheWinner(6,5))