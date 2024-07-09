from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time=0
        total=0
        for i in customers:
            if i[0]>time:
                time=i[0]
            time+=i[1]
            total+=time-i[0]
        return total/len(customers)
y

if __name__=='__main__':
    s = Solution()
    # print(s.averageWaitingTime([[1,2],[2,5],[4,3]]))
    # print(s.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
    print(s.averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]))