class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=root
        while curr:
            if p.val>curr.val and q.val>curr.val:
                curr=curr.right
            if p.val<curr.val and q.val<curr.val:
                curr=curr.left
            else:
                return curr


# Solution.lowestCommonAncestor(TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(0),TreeNode(8))),TreeNode(5),TreeNode(1))


if __name__ == "__main__":
    # Create tree nodes
    n1 = TreeNode(6)
    n2 = TreeNode(2)
    n3 = TreeNode(8)
    n4 = TreeNode(0)
    n5 = TreeNode(4)
    n6 = TreeNode(7)
    n7 = TreeNode(9)
    n8 = TreeNode(3)
    n9 = TreeNode(5)

    # Construct the tree
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n5.left = n8
    n5.right = n9
    n3.left = n6
    n3.right = n7

    # Create an instance of Solution
    solution = Solution()

    # Call lowestCommonAncestor method
    # lca = solution.lowestCommonAncestor(TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(0),TreeNode(8))),TreeNode(5),TreeNode(1))
    lca = solution.lowestCommonAncestor(TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(0),TreeNode(8))),TreeNode(5),TreeNode(4))
    print("Lowest Common Ancestor:", str(lca.val))