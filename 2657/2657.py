class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        one = set()
        both = 0
        ans = []
        n = len(A)
        for i in range(n):
            if A[i]==B[i]: both+=1
            else:
                if A[i] in one:
                    both+=1
                    one.remove(A[i])
                else: one.add(A[i])
                if B[i] in one:
                    both+=1
                    one.remove(B[i])
                else: one.add(B[i])
            ans.append(both)
        return ans 
        
