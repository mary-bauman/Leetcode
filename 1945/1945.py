class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(c) - 96) for c in s)
        for _ in range(k): s = str(sum(map(int, s)))
        return int(s)
         
