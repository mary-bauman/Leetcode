class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        smallestNum = min(nums)
        startingIndexOptions = [i for i, val in enumerate(nums) if val == smallestNum]
        #if any options work we return true
        def optionWorks(start):
            if start==0:
                return sorted(nums)==nums
            i = start
            while i < n-1:
                if nums[i+1]<nums[i]: #next one is decreased
                    return False
                i+=1
            #now i = n-1
            if nums[0] < nums[i]: return False
            i = 0
            while i < start-1:
                if nums[i+1]<nums[i]: #next one is decreased
                    return False
                i+=1
            #i is at the end with no issue
            return True

        for start in startingIndexOptions:
            if optionWorks(start): return True

        return False
