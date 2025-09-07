class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1: return [0]
        if n%2==0: return [x for i in range(1, n//2 + 1) for x in (i, -i)]
        return [x for i in range(1, n//2 + 1) for x in (i, -i)]+[0]
