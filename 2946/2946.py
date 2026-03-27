class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        numRows = len(mat)
        numCols = len(mat[0])
        for evenRow in range(0,numRows,2):
            row = mat[evenRow]
            for col in range(numCols):
                if row[col] != row[(col - k) % numCols]:
                    return False
        
        for oddRow in range(1,numRows,2):
            row = mat[oddRow]
            for col in range(numCols):
                if row[col] != row[(col + k) % numCols]:
                    return False
                
        return True
