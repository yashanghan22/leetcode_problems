from typing import List


class Solution:
    step = 0
    visited = set()

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if not 0 <= entrance[0] < len(maze) or not 0 <= entrance[1] < len(maze[0]) or maze[entrance[0]][entrance[1]] == '+':
            return self.step
        if entrance[0] == 0 or entrance[1] == len(maze[0])-1:
            print('0-0-0-0')
            return self.step
        ent = entrance
        self.visited.add((entrance[0], entrance[1]))
        for i, j in [(entrance[0]-1, entrance[1]), (entrance[0]+1, entrance[1]), (entrance[0], entrance[1]-1), (entrance[0], entrance[1]+1)]:
            if (i, j) not in self.visited:
                print(i, j)
                self.nearestExit(maze, [i, j])
        self.step += 1
        return self.step


if __name__ == '__main__':
    solution = Solution()
    # exit = solution.nearestExit(
    #     [[[".", "+"]]], [0, 0])
    exit = solution.nearestExit(
        [["+", "+", ".", "+"],
         [".", ".", ".", "+"],
         ["+", "+", "+", "."],], [1, 2])
    # exit = solution.nearestExit(
    #     [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0])
    print(exit)
