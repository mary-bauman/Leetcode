class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        c1 = Counter(s1)
        window = Counter(s2[:n1])
        
        if window == c1: return True
        
        for i in range(n1, n2):
            window[s2[i]] += 1
            window[s2[i - n1]] -= 1
            
            if window == c1: return True
            
        return False
