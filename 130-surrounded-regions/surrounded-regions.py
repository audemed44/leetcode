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
            if (row,0) in visited or board[row][0] == "O":
                dfs(row,0)
            if (row,COLS-1) in visited or board[row][COLS-1] == "O":
                dfs(row,COLS-1)
        for col in range(COLS):
            if (0, col) in visited or board[0][col] == "O":
                dfs(0,col)
            if (ROWS-1,col) in visited or board[ROWS-1][col] == "O":
                dfs(ROWS-1,col)
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) not in visited:
                    board[row][col] = "X"

        