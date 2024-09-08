from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length,curr=0,head
        while curr:
            curr=curr.next
            length+=1
        base_len,remainder=length//k,length%k
        curr=head
        res=[]
        for i in range(k):
            res.append(curr)
            for j in range(base_len-1+(1 if remainder else 0)):
                if not curr: break
                curr=curr.next
            remainder-=(1 if remainder else 0)
            if curr:
                curr.next,curr=None,curr.next
        return res


if __name__=='__main__':
    s = Solution()
    # print(s.splitListToParts(ListNode(1,ListNode(2,ListNode(3))),5))
    print(s.splitListToParts(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7,ListNode(8,ListNode(9,ListNode(10)))))))))),3))