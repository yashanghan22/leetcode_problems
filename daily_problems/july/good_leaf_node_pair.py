from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs=0
        # left_node=defaultdict(int)
        # right_node=defaultdict(int)
        def dfs(node:Optional[TreeNode]):
            if not node:
                return defaultdict(int)
            if not node.left and not node.right:
                count=defaultdict(int)
                count[1]=1
                return count
            left_dist=dfs(node.left)
            right_dist=dfs(node.right)

            for d1 in left_dist:
                for d2 in right_dist:
                    if d1+d2 <=distance:
                        self.pairs+=left_dist[d1]*right_dist[d2]
            
            all_dist=defaultdict(int)
            for d in left_dist:
                if d+1<=distance:
                    all_dist[d+1]+=left_dist[d]
            for d in right_dist:
                if d+1<=distance:
                    all_dist[d+1]+=right_dist[d]
            return all_dist
        dfs(root)
        return self.pairs


if __name__=='__main__':
    s = Solution()
    print(s.countPairs(TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7))),distance=3))