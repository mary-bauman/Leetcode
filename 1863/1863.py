from functools import reduce
from operator import ixor

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return sum(reduce(ixor, subset) for subset in chain.from_iterable(combinations(nums, r) for r in range(1, len(nums) + 1)))

