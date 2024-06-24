class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float('inf')]*(len(word2)+1) for i in range(len(word1)+1)]
        for j in range(len(word2)+1):
            cache[len(word1)][j] = len(word2)-j
        for i in range(len(word1)+1):
            cache[i][len(word2)] = len(word1)-i
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                # print(i+1, j+1)
                # print(cache)
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    print(cache[i+1][j], cache[i]
                          [j+1], cache[i+1][j+1])
                    cache[i][j] = 1+min(cache[i+1][j], cache[i]
                                        [j+1], cache[i+1][j+1])
        # print(cache)
        return cache[0][0]


if __name__ == '__main__':
    solution = Solution()
    # var = [[3, 3, 4, 5], [3, 2, 3, 4], [2, 2, 2, 3],
    #        [3, 2, 1, 2], [3, 2, 1, 1], [3, 2, 1, 0],]
    mind = solution.minDistance('horse', 'ros')
    # mind = solution.minDistance('intention', 'execution')
    print(mind)
