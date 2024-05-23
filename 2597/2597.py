class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(nums,k,i,s) -> int:
            if i >= len(nums): return 1 if s else 0
            count = dfs(nums, k, i+1, s)
            if (nums[i]-k) in s: return count
            return count + dfs(nums, k, i+1, (s | {nums[i]}))

        return dfs(sorted(nums),k,0,set())


        
