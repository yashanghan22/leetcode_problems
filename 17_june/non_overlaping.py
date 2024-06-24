from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlap = {}
        remove = 0
        for i in intervals:
            if not list(overlap.keys()).__contains__(i[0]):
                overlap[i[0]] = i[1]
            else:
                remove += 1
        print(overlap)
        return remove


if __name__ == '__main__':
    solution = Solution()
    erase = solution.eraseOverlapIntervals([[1, 2], [2, 3]])
    # erase = solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
    # erase = solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
    print(erase)
