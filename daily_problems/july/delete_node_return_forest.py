from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete=set(to_delete)
        res_set=set([root])
        def dfs(node: Optional[TreeNode]):
            if not node:
                return None
            res=node
            if node.val in to_delete:
                res=None
                res_set.discard(node)
                if node.left: res_set.add(node.left)
                if node.right: res_set.add(node.right)
            node.left=dfs(node.left)
            node.right=dfs(node.right)
            return res
        dfs(root)
        return list(res_set)


if __name__=='__main__':
    s = Solution()
    print(s.delNodes(TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7))), [3,5]))