class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]>0 or nums[-1]<0: 
            #all positive OR all negative
            return nums[-1]*nums[-2]*nums[-3]
        elif nums[-1]==0: return 0
        else:
            #only care about 2 lowest and 3 highest
            ans = nums[-1]*nums[-2]*nums[-3]
            ans = max(ans, nums[0]*nums[1]*nums[-1])

            return ans
