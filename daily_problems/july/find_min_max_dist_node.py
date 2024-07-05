from typing import Optional,List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def isCritical(prev: Optional[ListNode],cur: Optional[ListNode],nxt: Optional[ListNode])->bool:
            return (prev.val<cur.val>nxt.val or prev.val>cur.val<nxt.val)
        prev,cur=head,head.next
        nxt=cur.next
        min_dis=float('inf')
        max_dis=-1

        prev_crit_inx=0
        first_crit_inx=0
        inx=1

        while nxt:
            if isCritical(prev,cur,nxt):
                if first_crit_inx:
                    max_dis=inx-first_crit_inx
                    min_dis=min(min_dis,inx-prev_crit_inx)
                else:
                    first_crit_inx=inx
                prev_crit_inx=inx
            prev,cur,nxt=cur,nxt,nxt.next
            inx+=1
        
        if min_dis==float('inf'):
            min_dis=-1

        return [min_dis,max_dis]

if __name__=='__main__':
    solution=Solution()
    # print(solution.nodesBetweenCriticalPoints(ListNode(3,next=ListNode(1))))
    # [5,3,1,2,5,1,2]
    print(solution.nodesBetweenCriticalPoints(ListNode(5,next=ListNode(3,next=ListNode(1,next=ListNode(2,next=ListNode(5,next=ListNode(1,next=ListNode(2)))))))))