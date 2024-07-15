from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node=TreeNode()
        nodes={}
        children=set()
        
        for par,child,is_left in descriptions:
            children.add(child)
            if par not in nodes:
                nodes[par]=TreeNode(par)
            if child not in nodes:
                nodes[child]=TreeNode(child)
            if is_left:
                nodes[par].left=nodes[child]
            else:
                nodes[par].right=nodes[child]
        for p,c,l in descriptions:
            if p not in children:
                return nodes[p]
        return node

if __name__=='__main__':
    s=Solution()
    print(s.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]).val)