class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def search(r,c):
            q = deque()
            q.append((r,c))
            while q:
                i, j = q.popleft() # this is bfs, change to pop() for dfs
                if (i >= 0 and
                    j >= 0 and
                    i < len(grid) and
                    j < len(grid[0]) and
                    grid[i][j] == "1" and
                    (i,j) not in visited):
                    visited.add((i,j))
                    q.append((i-1,j))
                    q.append((i+1,j))
                    q.append((i,j-1))
                    q.append((i,j+1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    islands += 1
                    search(row,col)
        return islands
        