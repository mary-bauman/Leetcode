class KthLargest:
    def __init__(self, k: int, nums: List[int]): self.nums, self.k = sorted(nums, reverse=True), k
    def add(self, val: int) -> int:
        self.nums+=[val]
        return sorted(self.nums, reverse=True)[self.k-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
