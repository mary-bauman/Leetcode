class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        done = set()
        n = len(nums)
        for i in range(n-1,-1,-1):
            if nums[i] in done:
                #ceiling = upside down floor
                return (-((i+1) // -3))
            else: done.add(nums[i])

        return 0
