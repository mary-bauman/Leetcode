class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = set()
        q = deque()
        m = len(grid)
        n = len(grid[0])
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1' and (y,x) not in visited:
                    ans += 1
                    q.append((y,x))
                    visited.add((y,x))
                    while q:
                        yPos, xPos = q.popleft()
                        if yPos > 0 and grid[yPos-1][xPos] == '1' and (yPos-1, xPos) not in visited:
                            q.append((yPos-1, xPos))
                            visited.add((yPos-1, xPos))
                        if yPos < m-1 and grid[yPos+1][xPos] == '1' and (yPos+1, xPos) not in visited:
                            q.append((yPos+1, xPos))
                            visited.add((yPos+1, xPos))
                        if xPos > 0 and grid[yPos][xPos-1] == '1' and (yPos, xPos-1) not in visited:
                            q.append((yPos, xPos-1))
                            visited.add((yPos, xPos-1))
                        if xPos < n-1 and grid[yPos][xPos+1] == '1' and (yPos, xPos+1) not in visited:
                            q.append((yPos, xPos+1))
                            visited.add((yPos, xPos+1))
        return ans                
