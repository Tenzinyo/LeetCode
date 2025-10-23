def num_islands(self,grid):
    if not grid:
        return 0
    visited = set()
    rows, cols = len(grid), len(grid[0])
    
    def bfs(r,c):
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c))
        while q:
            row,col = q.popleft() #lifo
            dir = [[0,1],[0,-1],[-1,0],[1,0]]
            for dr,dc in dir:
                h = dr + row
                v = dc + col
                if (h in range(rows) and v in range(cols) and grid[h][v]== "1" and (h,v) not in visited):
                    q.append((h,v))
                    visited.add((h,v))
                # check if its inbound, before visting the nodes
                
                
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)
                islands += 1
    return islands