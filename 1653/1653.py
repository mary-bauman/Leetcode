class Solution:
    def minimumDeletions(self, s: str) -> int:
        bs = 0
        minDeletions = 0
        for char in s:
            if char == 'a':
                minDeletions = min(minDeletions + 1, bs)
            else:
                bs += 1   
        return minDeletions
