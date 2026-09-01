from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use bfs for matrix
        # create rows and cols
        # create q
        # create directions

        # 1 = island
        # 0 = water

        rows , cols = len(grid), len(grid[0])
        islands = 0 # result
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(r,c):
            q = deque()
            # KEY2: mark this spot as visited
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # KEY1: continue when it's out of bound or "0"
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        # KEY2: mark this spot as visited
                        grid[nr][nc] = "0"

                    # if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0":
                    #     continue

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # KEY3: recursive find the neibors until it's all count
                    bfs(r,c)
                    islands += 1
        
        return islands