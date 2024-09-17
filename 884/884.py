class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = []
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        for c in c1:
            if c1[c] == 1 and c not in c2: words.append(c)
        for c in c2:
            if c2[c] == 1 and c not in c1: words.append(c)

        return words
        
