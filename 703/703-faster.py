class KthLargest:
    def __init__(self, k: int, nums: List[int]): 
        nums.sort(reverse=True)
        self.nums, self.cur, self.k = nums, -inf, k

    def add(self, val: int) -> int:
        if val > self.cur:
            self.nums+=[val]
            self.nums.sort(reverse=True)
            self.cur = self.nums[self.k-1]
        return self.cur


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
