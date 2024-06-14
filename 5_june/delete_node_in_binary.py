from typing import List, Optional
from lowest_common_ance_python import TreeNode 



class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        print('====================')
        curr=root
        left=curr.left
        right=curr.right
        print(root.val)
        if curr.val==key:
            print('current val is equals to key')
            if left:
                curr.val=left.val
                curr.left=None
            if right:
                curr.val=right.val
                curr.right=None
            return curr
        else:
            if left:
                self.deleteNode(left,key=key)
            if right:
                self.deleteNode(right,key=key)
        print('return',curr.val)
        return curr

if __name__=='__main__':
    solution=Solution()
    node=TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6,None,TreeNode(7)))
    val=solution.deleteNode(node,3)
    # print('solution search BST:'+str(val))
    if val is not None:
        print('solution search BST:'+str(val.val))
    else:
        print('search BST cannot find node from given value')

