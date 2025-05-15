"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            arr = []
            for c in node.children:
                arr += dfs(c)
            arr.append(node.val)
            return arr
        return dfs(root) if root else []
