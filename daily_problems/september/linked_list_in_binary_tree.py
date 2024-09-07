from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self.helper(head,root):
            return True
        if not root:
            return False
        return (self.isSubPath(head,root.left) or self.isSubPath(head,root.right))

    def helper(self,list_node,tree_node):
        if not list_node:
            return True
        if not tree_node or list_node.val!=tree_node.val:
            return True
        return (self.helper(list_node.next,tree_node.left) or self.helper(list_node.next,tree_node.right))

if __name__=='__main__':
    s = Solution()
    head=ListNode(4,ListNode(2,ListNode(8)))
    root=TreeNode(1,TreeNode(4,None,TreeNode(2,None,TreeNode(1))),TreeNode(4,TreeNode(2,TreeNode(6),TreeNode(8,TreeNode(1),TreeNode(3)))))
    print(s.isSubPath(head,root))