class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for n in nums:
            s = 0
            n2 = n
            while n2:
                s += n2 % 10
                n2 //= 10
            d[s].append(n)

        maxSum = -1
        for key in d:
            a = d[key]
            if len(a)>1:
                maxSum = max(maxSum, sum(heapq.nlargest(2, a)))

        return maxSum
