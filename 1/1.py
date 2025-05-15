class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)-1):
            if (target-nums[n]) in nums[n+1:]:
                return [n, n+1 + nums[n+1:].index((target-nums[n]))]
