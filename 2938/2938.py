class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        blackDists = [(n-1-i) for i in range(n-1,-1,-1) if s[i]=='1']

        blacks = 0
        for b in range(len(blackDists)):
            if blackDists[b]!=b:
                blacks += abs(blackDists[b]-b)

        return blacks
