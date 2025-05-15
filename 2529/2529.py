class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        #one liner
        return max(sum(1 for n in nums if n<0), sum(1 for n in nums if n>0))


        #fast solution, beats 100% at runtime
        pos = 0
        neg = 0
        for n in nums:
            if n<0: neg+=1
            elif n>0: pos+=1
        return max(pos,neg)
