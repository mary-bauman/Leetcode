class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = [str(n) for n in nums]
        #lambda function to compare (a + b and b + a), taking larger number order.
        s.sort(key=lambda a: a*10, reverse=True)
        return "".join(s) if s[0]!="0" else "0"
