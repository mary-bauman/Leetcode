# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(cur):
            if cur.val == 0 or cur.val == 1:
                return cur.val == 1
            elif cur.val == 2:
                return helper(cur.left) or helper(cur.right)
            elif cur.val == 3:
                return helper(cur.left) and helper(cur.right)
            return False
        return helper(root)
