# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    pick = 1

    def guess(self, num: int) -> int:
        if self.pick < num:
            return -1
        elif self.pick > num:
            return 1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        lst=[i for i in range(1,n)]
        print(lst)
        if len(lst)==1:
            return 1
        for i in range(1, n):
            val = self.guess(i)
            if val == 0:
                print(val)
                return i
        return 0


if __name__ == '__main__':
    val = Solution().guessNumber(1)
    print(val)
