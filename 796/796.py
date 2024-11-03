class Solution:
    def rotateString(self, cur: str, goal: str) -> bool:
        prev = set()
        while cur not in prev:
            if cur==goal: return True

            prev.add(cur)
            cur = cur[1:] + cur[0]
            
        return False
