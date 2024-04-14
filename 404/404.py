# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        left = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    if not node.left.left and not node.left.right:
                        left+=node.left.val
                    else:
                        queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return left
