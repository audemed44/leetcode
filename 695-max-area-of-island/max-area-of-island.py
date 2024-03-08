class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r,c):
            if (r < 0 
            or c < 0 
            or r == rows 
            or c == cols 
            or grid[r][c]==0 
            or (r,c) in visited):
                return 0
            visited.add((r,c))
            return (1 + dfs(r+1,c)
                      + dfs(r-1,c)
                      + dfs(r,c+1)
                      + dfs(r,c-1))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    max_area = max(max_area,dfs(row,col))
        return max_area