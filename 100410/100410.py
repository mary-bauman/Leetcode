class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        a = ord(c1[0])-96
        b = int(c1[1])
        x = ord(c2[0])-96
        y = int(c2[1])
        return (a+b)%2 == (x+y)%2
