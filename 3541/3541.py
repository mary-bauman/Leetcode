class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        vowel = max((c['a'],c['e'],c['i'],c['o'],c['u']), default=0)
        del c['a']
        del c['e']
        del c['i']
        del c['o']
        del c['u']
        cons = max(c.values(), default=0)
        return vowel + cons
