from typing import List, Optional
from lowest_common_ance_python import TreeNode 

class Solution:
    level=1
    sum=0
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return self.level
        self.sum=root.val
        left=0
        right=0
        if root.left:
            left=root.left.val
        if root.right:
            right=root.right.val
        # while root.right or root.left:
        #     left=root.left.val
        #     right=root.right.val


        # if root:
        # self.level+=1
        # if self.sum<root.val:
        # if self.level==1:
        #     self.sum=root.val
        #     self.level+=1
        # else:
        #     return self.a
        # left= self.maxLevelSum(root=root.left)
        # right=self.maxLevelSum(root=root.right)
        # if(root.left.val+root.right.val>self.sum):
        #     self.sum=root.left.val+root.right.val
        #     print("left:"+str(root.left.val)+",right:"+str(root.right.val)+",sum:"+str(self.sum))
        #     self.level+=1
        #     self.maxLevelSum(root=root.left)
        #     self.maxLevelSum(root=root.right)
        if(left+right>self.sum):
            self.sum=left+right
            print("left:"+str(left)+",right:"+str(right)+",sum:"+str(self.sum))
            self.level+=1
            self.maxLevelSum(root=root.left)
            self.maxLevelSum(root=root.right)
        return self.level
    

if __name__=='__main__':
    solution=Solution()
    # node=TreeNode(1,TreeNode(7,TreeNode(7),TreeNode(-8)),TreeNode(0))
    node=TreeNode(989,None,TreeNode(10250,TreeNode(98693,None,TreeNode(-32127)),TreeNode(-89388)))
    val=solution.maxLevelSum(node)
    print('max level sum level:'+str(val))


    # [989,null,10250,98693,-89388,null,null,null,-32127]