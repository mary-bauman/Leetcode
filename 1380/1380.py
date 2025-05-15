class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        luckyRow = set(min(row) for row in matrix)
        luckyCol = set()
        for col in range(cols):
            luckyCol.add(max([matrix[row][col] for row in range(rows)]))
        return luckyRow & luckyCol

      #one liner version
      #return {min(row) for row in matrix} & {max(row[col] for row in matrix) for col in range(len(matrix[0]))}
    
