from typing import List, Optional
from lowest_common_ance_python import TreeNode 

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        curr=root
        if curr is None:
            print('root is None')
            return curr
        if curr.val==val:
            print('root',curr.val)
            return curr
        else:
            left=self.searchBST(curr.left,val=val)
            right=self.searchBST(curr.right,val=val)
            if left and left.val==val:
                return left
            if right and right.val==val:
                return right
            return None
        # if curr.val==val:
        #     return curr
        # else:
        #     return None
    

if __name__=='__main__':
    solution=Solution()
    node=TreeNode(4,TreeNode(7,TreeNode(1),TreeNode(3)),TreeNode(2))
    val=solution.searchBST(node,2)
    # print('solution search BST:'+str(val))
    if val is not None:
        print('solution search BST:'+str(val.val))
    else:
        print('search BST cannot find node from given value')

