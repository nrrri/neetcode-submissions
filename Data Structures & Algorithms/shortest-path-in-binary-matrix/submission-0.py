class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # use bfs matrix
        # if no clear path return -1
        # grid is N*N
        # find path from [0][0] to [n-1][n-1]
        
        # create size
        N = len(grid)
        # create directions (8 directions)
        directions = [[0,1],[0,-1],[-1,0],[1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

        if grid[0][0] or grid[N-1][N-1]:
            return -1

        # KEY1: save length in q and start = (0,0)
        q = deque([(0,0,1)]) # start (0,0) length = 1
        visited = set([(0,0)]) # start at (0,0)    
        while q:
            r,c, length = q.popleft()
            # KEY2: [N-1][N-1] = finish
            if r == N-1 and c == N-1:
                return length

            for dr,dc in directions:
                nr,nc = r + dr, c+ dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0 and (nr,nc) not in visited: # check the grid is in condition
                    q.append((nr,nc, length + 1))   # add new q
                    visited.add((nr,nc))            # update visited

        return -1