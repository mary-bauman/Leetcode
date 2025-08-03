class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        #look for hills
        for i in range(1,len(nums)-1):
            start = nums[i-1]
            n = nums[i]
            if start < n:
                #it starts out as a hill, lets find out if it ends as one
                while i < len(nums) and nums[i]==n: i+=1
                if i < len(nums) and nums[i] < n:
                    # print(f"hill found starting at {start}, peaking at {n}, and ending at {nums[i]}")
                    ans += 1
        #look for valleys
        for i in range(1,len(nums)-1):
            start = nums[i-1]
            n = nums[i]
            if start > n:
                #it starts out as a valley, lets find out if it ends as one
                while i < len(nums) and nums[i]==n: i+=1
                if i < len(nums) and nums[i] > n:
                    # print(f"valley found starting at {start}, peaking at {n}, and ending at {nums[i]}")
                    ans += 1


        return ans
