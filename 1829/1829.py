from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        m = (1 << maximumBit) - 1
        curXor = reduce(ixor, nums, 0)
        ans = []
        
        for num in reversed(nums):
            ans.append(curXor ^ m)  # Maximize XOR with `m`
            curXor ^= num  # Remove the last element from XOR as we pop
        
        return ans
