class Solution:
    def maximumSwap(self, num: int) -> int:
        total = num
        s = str(num)
        for a in range(len(s)-1):
            for b in range(a+1,len(s)):
                newS = int(s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:])
                if newS > total: total = newS   
        return total
