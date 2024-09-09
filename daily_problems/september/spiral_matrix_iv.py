from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res=[[-1]*n for _ in range(m)]
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        x,y,i=0,0,0
        while head:
            res[x][y]=head.val
            head=head.next
            next_x = x + direction[i][0]
            next_y = y + direction[i][1]
            
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or res[next_x][next_y] != -1:
                i = (i + 1) % 4
                next_x = x + direction[i][0]
                next_y = y + direction[i][1]
            
            x, y = next_x, next_y
        return res

if __name__=='__main__':
    s = Solution()
    print(s.spiralMatrix(3, 5, ListNode(3,ListNode(0,ListNode(2,ListNode(6,ListNode(8,ListNode(1,ListNode(7,ListNode(9,ListNode(4,ListNode(2,ListNode(5,ListNode(5,ListNode(0)))))))))))))))