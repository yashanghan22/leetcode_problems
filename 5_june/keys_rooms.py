from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        list = [0 for _ in range(len(rooms))]
        keySet = set()
        for i in range(0, len(rooms)):
            if i == 0:
                list[i] = 1
                keySet.update(rooms[i])
            if keySet.__contains__(i):
                list[i] = 1
                keySet.update(rooms[i])
            # for k in range(len(rooms[i])):
            #     if rooms[i][k]<i:
            #         print("-=-=->"+str(k))
            #         list[rooms[i][k]]=1
            #     keySet.update(rooms[i])
        print(list)
        print(keySet)
        return not list.__contains__(0)


if __name__ == '__main__':
    solution = Solution()
    romms = solution.canVisitAllRooms([[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]])
    # romms = solution.canVisitAllRooms([[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]])
    # romms = solution.canVisitAllRooms([[2],[],[1]])
    # romms = solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
    # romms = solution.canVisitAllRooms([[1], [2], [3], []])
    print(romms)
