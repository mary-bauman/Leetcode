class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.target = target
        self.nums = nums
        self.n = len(nums)
        self.memo = dict()
        def checkExpression(total, i):
            if i == self.n: return int(total==self.target)
            if (total,i) not in self.memo: self.memo[(total, i)] = checkExpression(total-self.nums[i], i+1) + checkExpression(total+self.nums[i], i+1)            
            return self.memo[(total, i)]
        return checkExpression(0, 0)
