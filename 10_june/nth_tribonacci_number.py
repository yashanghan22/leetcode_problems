class Solution:
    def tribonacci(self, n: int) -> int:
        res = []
        for i in range(n+1):
            if i == 0 or i == 1:
                res.append(i)
            else:
                if len(res) < 4:
                    res.append(sum(res))
                else:
                    sm = res[i-1]+res[i-2]+res[i-3]
                    res.append(sm)
        return res[n]


if __name__ == '__main__':
    solution = Solution()
    trib = solution.tribonacci(26)
    print(trib)
