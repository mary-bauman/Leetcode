class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        low = defaultdict(list)
        up = defaultdict(list)
        for wi,w in enumerate(word):
            (low if w.islower() else up)[w].append(wi)
        
        return sum(1 for letter, nums in low.items() if up.get(letter.upper(), []) and min(up.get(letter.upper(), [])) > max(nums))
