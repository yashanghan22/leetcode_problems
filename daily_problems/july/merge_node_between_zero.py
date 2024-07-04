# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur.next:
            node=cur.next
            cur=cur.next
            while cur.next.val!=0:
                node.val+=cur.next.val
                cur=cur.next
            cur=cur.next
            node.next=cur.next
        return head.next


if __name__=="__main__":
    solution=Solution().mergeNodes(ListNode(
        val=0,
        next=ListNode(
            val=3,
            next=ListNode(
            val=1,next=ListNode(
            val=0,next=ListNode(
            val=4,next=ListNode(
            val=5,next=ListNode(
            val=2,next=ListNode(
            val=0
        )
        )
        )
        )
        )
        )
        )
    ))
    print("-=>"+str(solution.val))