class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        modify matrix in-place
        """
        r = set()
        c = set()
        m = len(matrix)
        n = len(matrix[0])
        for a in range(m):
            for b in range(n):
                if matrix[a][b]==0:
                    r.add(a)
                    c.add(b)
        
        for a in r:
            matrix[a] = [0]*n
        for b in c:
            for a in range(m):
                matrix[a][b]=0
        
