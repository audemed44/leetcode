class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r,c):
            if ((r,c) in visited 
            or r < 0 or c < 0 
            or r==ROWS or c==COLS
            or board[r][c]=="X"):
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for row in range(ROWS):
            dfs(row,0)
            dfs(row,COLS-1)
        for col in range(COLS):
            dfs(0,col)
            dfs(ROWS-1,col)
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) not in visited:
                    board[row][col] = "X"

        