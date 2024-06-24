from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow = points
        count = 0
        for i in range(len(points) + 1):
            # print(points[i:])
            lst = points[i:]
            for j in range(1, len(points[i:])):
                # print(lst[j])
                ran = range(points[i][0], points[i][1]+1)
                if points[i] != lst[j] and lst[j] in arrow and (lst[j][0] in ran or lst[j][1] in ran):
                    arrow.remove(lst[j])
                    count += 1
                # if points[i] != lst[j] and (points[i][1] <= lst[j][0]):
                #     # points[i][0] >= lst[j][1] or
                #     print(points[i], lst[j])
                #     arrow.remove(lst[j])
                    # if lst[j] not in arrow:
                    #     arrow.append(lst[j])
                    # if points[i] not in arrow and lst[j] not in arrow:
                    #     # print(points[i], points[j])
                    #     arrow.append(points[i])
                    #     arrow.append(lst[j])
                    #     count += 1
                    # if points[i] not in arrow:
                    #     arrow.append(points[i])
                    #     count += 1
                    # if lst[j] not in arrow:
                    #     count += 1
                    #     arrow.append(lst[j])
        # print((arrow))
        return len(arrow)


if __name__ == "__main__":
    solution = Solution()
    findMin = solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]])
    # findMin = solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]])
    # findMin = solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
    print(findMin)
