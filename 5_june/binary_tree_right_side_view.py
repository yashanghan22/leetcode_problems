from typing import List, Optional
from lowest_common_ance_python import TreeNode 

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root: return []

        nodeList=[]
        curr=root
        while curr :
            nodeList.append(curr.val)
            if curr.right and curr.left.left and curr.right.right:
                curr=curr.left
            else:
                curr=curr.right
        return nodeList
    


if __name__=='__main__':
    solution=Solution()
    node=TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3,None,TreeNode(4)))
    val=solution.rightSideView(node)
    print('solution of right side view'+str(val))
