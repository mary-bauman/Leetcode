class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        #increasing
        best = 0
        past = -inf
        cur = 0
        #increasing
        for i in range(len(nums)):
            if nums[i]>past:
                print(nums[i])
                cur+=1
            else:
                best = max(best, cur)
                cur = 1
            past = nums[i]
        best = max(best, cur)
        past = inf
        cur = 0
        #decreasing
        for i in range(len(nums)):
            if nums[i]<past:
                cur+=1
            else:
                best = max(best, cur)
                cur = 1
            past = nums[i]
        best = max(best, cur)


        return best
