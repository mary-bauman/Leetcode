class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gentry(root: int, mini=1, maxi=n+1) -> List[Optional[TreeNode]]:
            left = []
            right = []

            for l in range(mini, root):
                left += gentry(l, mini, root)
            
            for r in range(root+1, maxi):
                right += gentry(r, root+1, maxi)

            if not left and not right:
                return [TreeNode(root)]

            if not left:
                return [TreeNode(root, None, r) for r in right]           
            
            if not right:
                return [TreeNode(root, l, None) for l in left]                    
            
            return [TreeNode(root, l, r) for l in left for r in right]
        
        ans = []
        for i in range(n):
            ans += gentry(i+1)
        
        return ans
