# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    pick = 5

    def guess(self, num: int) -> int:
        if self.pick < num:
            return -1
        elif self.pick > num:
            return 1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        for i in range(1, n):
            val = self.guess(i)
            if val == 0:
                return i
        return 0


if __name__ == '__main__':
    val = Solution().guessNumber(8)
    print(val)
