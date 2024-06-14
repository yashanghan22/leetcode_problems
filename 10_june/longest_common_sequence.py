class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp = [[_ for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        # print(dp)
        # for i in range(len(text1)-1, -1, -1):
        #     for j in range(len(text2)-1, -1, -1):
        #         if text1[i] == text2[j]:
        #             print(i, j)
        #             print(dp[i+1][j+1])
        #             dp[i][j] = 1+dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # print(dp[0][0])
        seq = []
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j] and text1[i] not in seq:
                    # print(text1[i])
                    seq.append(text1[i])
                    print(seq)
        # print(seq)
        return len(seq)


if __name__ == '__main__':
    solution = Solution()
    long = solution.longestCommonSubsequence('abcde', 'ace')
    print(long)
