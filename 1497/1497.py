class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = Counter([a%k for a in arr])
        if c[0]%2==1: return False
        del c[0]
        for d in c:
            if c[d]!=c[k-d]: return False
            
        return True
