from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        combi = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if len(digits) == 1:
            return combi[digits]
        count = 1
        res = []
        finRes = set()
        for i in digits:
            res.append(combi[i])
        while count < len(digits):
            for u in res[0]:
                for v in res[count]:
                    finRes.add(u+v)
            count += 1
        return list(finRes)


if __name__ == '__main__':
    solution = Solution()
    letter = solution.letterCombinations('5623')
    print(letter)
