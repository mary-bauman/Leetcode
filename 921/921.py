class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lefts = 0
        adds = 0
        for c in s:
            if c=='(': lefts+=1
            elif lefts: lefts-=1
            else: adds+=1
        return adds + lefts
