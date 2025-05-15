class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        for a in range(n):
            for b in range(a): d[nums[a]*nums[b]] += 1
            for b in range(a+1, n): d[nums[a]*nums[b]] += 1

        return sum([d[di] * (d[di]-2) for di in d])
