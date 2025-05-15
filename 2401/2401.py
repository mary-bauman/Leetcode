class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        best = 1
        n = len(nums)
        bn = (len(bin(max(nums)))-2)
        for start in range(n):
            b = bin(nums[start])[2:]
            bLen = len(b)
            cur = [0] * bn
            for i in range(bLen):
                cur[i + bn - bLen] += int(b[i])
            
            for end in range(start+1,n):
                e = bin(nums[end])[2:]
                eLen = len(e)
                for i in range(eLen):
                    cur[i + bn - eLen] += int(e[i])
                
                if 2 in cur:
                    best = max(best, end-start)
                    break

            if 2 not in cur:
                best = max(best, n-start)
            


        return best
