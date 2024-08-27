from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        if not root:
            return []
        stack=[(root,False)]

        while stack:
            node,visited=stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append((node,True))
                for c in node.children[::-1]:
                    stack.append((c,False))
        return res


if __name__=='__main__':
    s = Solution()
    print(s.postorder(Node(1,Node(None,Node(3,Node(4,Node(5,Node(None,Node(5,Node(6))))))))))