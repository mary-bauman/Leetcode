class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        return ([a for a in arr if arr.count(a)==1] + [""]*k)[k-1]
