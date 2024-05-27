class Solution:
    def specialArray(self, nums: List[int]) -> int:
        return next((i for i in range(0, max(nums) + 1) if i == sum(1 for n in nums if n >= i)), -1)

        
