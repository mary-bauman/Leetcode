class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #from the editorial 
        n = len(s)
        rs = s[::-1]
        for i in range(n):
            if s[:n-i] == rs[i:]:
                return rs[:i] + s
        return ""
