class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        cur = "0" * n
        while cur in nums:
            if cur[-1]=="0": cur = cur[:-1]+"1"
            else:
                rightMostZero = n-1
                while cur[rightMostZero]=="1": rightMostZero-=1
                cur = cur[:rightMostZero] + "1" + ("0" * (n-1-rightMostZero))
        return cur
