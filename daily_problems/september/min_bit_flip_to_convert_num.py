# "{0:b}".format(num)

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')

if __name__=='__main__':
    s = Solution()
    print(s.minBitFlips(10,7))