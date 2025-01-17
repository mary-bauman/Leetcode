class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a,b = 0,0
        if len(nums1)%2:
            for n in nums2: b^=n
        if len(nums2)%2:
            for n in nums1: a^=n

        return a ^ b

