class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific, atlantic = set(), set()
        res = []
        def dfs(r, c, visit, prev_h):
            if (r == ROWS or r < 0 or c == COLS or c < 0
            or heights[r][c] < prev_h or (r,c) in visit):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        for row in range(ROWS):
            dfs(row,0,pacific,heights[row][0])
            dfs(row,COLS-1,atlantic,heights[row][COLS-1])
        for col in range(COLS):
            dfs(0,col,pacific,heights[0][col])
            dfs(ROWS-1,col,atlantic,heights[ROWS-1][col])
        for (r,c) in pacific:
            if (r,c) in atlantic:
                res.append([r,c])
        return res