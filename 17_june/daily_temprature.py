from typing import List
import datetime


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # current_time = datetime.datetime.now()
        lst = [0]*len(temperatures)
        # res = [0]*len(temperatures)
        # stack = []
        # print(datetime.datetime.now())
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    # print(i, j)
                    lst[i] = j-i
                    break
        # print(lst)
        # for i, t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         stackT, stackInd = stack.pop()
        #         res[stackInd] = (i-stackInd)
        #     stack.append([t, i])
        # print(datetime.datetime.now())
        # print(res)
        return lst


if __name__ == '__main__':
    solution = Solution()
    # daily = solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    # daily = solution.dailyTemperatures([30, 40, 50, 60])
    daily = solution.dailyTemperatures([30, 60, 90])
    print(daily)
