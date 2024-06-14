class Solution:
    count = 0

    def uniquePaths(self, m: int, n: int) -> int:
        # direction = [(1, 0), (0, 1)]
        # mat = [[0 for _ in range(m)] for _ in range(n)]
        # print(mat)
        print(m, n)
        self.count += 1
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n)+self.uniquePaths(m, n-1)


if __name__ == '__main__':
    solution = Solution()
    unique = solution.uniquePaths(3, 3)
    print(unique)
    print(solution.count)
