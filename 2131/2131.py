class Solution:
    def longestPalindrome(self, words):
        c = Counter(words)
        middle = False
        ans = 0
        for w in c:
            rw = w[::-1]
            if w==rw:
                ans += (c[w] // 2) * 4
                if c[w]%2==1: middle = True
            elif rw in c:
                ans += min(c[w],c[rw]) * 2

        if middle: ans += 2
        return ans
