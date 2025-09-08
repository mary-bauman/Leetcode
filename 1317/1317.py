class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def findBig(big):
            while "0" in str(big): big-=1
            if "0" in str(n-big):
                return findBig(big-1)
            return big

        big = findBig(n-1)
        return([n-big,big])
