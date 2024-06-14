class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        # a, b, c = 5, 11, 24  # [a,b,c] => [b,c,a+c+c] => [b,c]+[2*c+a]
        a, b, c = 1, 2, 5    # [a,b,c] => [b,c,a+c+c] => [b,c]+[2*c+a]
        for i in range(3, n):
            a, b, c = b, c, 2*c+a
        print(c, 10**9+7)
        return c % (10**9+7)


if __name__ == '__main__':
    solution = Solution()
    tiling = solution.numTilings(4)
    print(tiling)
