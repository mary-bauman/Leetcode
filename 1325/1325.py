class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def nodesFixedUp(root, target):
            if not root:
                return None

            if not root.left and not root.right:
                return None if root.val == target else root

            root.left = nodesFixedUp(root.left, target)
            root.right = nodesFixedUp(root.right, target)

            return root if root.val != target or root.left or root.right else None
            
        return nodesFixedUp(root, target)
