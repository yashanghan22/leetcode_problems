class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if a | b == c:
            return 0
        flip = 0
        currA = a
        currB = b
        for i in range(1, a+2):
            for j in range(1, b+2):
                if i | j == c:
                    currA = i
                    currB = j
                    break
        # print(a, b)
        # print(currA, currB)
        # flip = (a-currA)+(b-currB)
        flip = (max(a, currA)-min(a, currA))+(max(b, currB)-min(b, currB))
        return flip


if __name__ == "__main__":
    solution = Solution()
    # minf = solution.minFlips(4, 2, 7)
    minf = solution.minFlips(2, 6, 5)
    print(minf)
