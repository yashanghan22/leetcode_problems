from typing import List,Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        dummy=ListNode(0,head)
        prev=dummy
        while prev.next:
            if prev.next.val in nums:
                prev.next=prev.next.next
            else:
                prev=prev.next
        return dummy.next
        # def dfs(node: Optional[ListNode]):
        #     if not node:
        #         return
        #     if node.val not in nums:
        #         print(node.val)
        #         if nde.val:
        #             nde.next=ListNode(val=node.val)
        #         else:
        #             nde.val=node.val
        #     #    return dfs(node.next)
        #     dfs(node.next)
        # dfs(head)
        # return nde


if __name__=='__main__':
    s = Solution()
    # print(s.modifiedList([1,2,3],ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))).val)
    # print(s.modifiedList([1],ListNode(1,ListNode(2,ListNode(1,ListNode(2,ListNode(1,ListNode(2))))))))
    print(s.modifiedList([5],ListNode(1,ListNode(2,ListNode(3,ListNode(4))))))