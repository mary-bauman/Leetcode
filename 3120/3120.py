class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return len(set(w for w in word if w.islower() and w.upper() in word))
        
        
