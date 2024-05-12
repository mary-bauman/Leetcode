class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        a = []
        for i in range(1,len(grid)-1):
            row = []
            for j in range(1,len(grid)-1):
                row.append(max([grid[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2)]))
            a.append(row)
        return a
