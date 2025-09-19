def islandPerimeter(self, grid: List[List[int]]) -> int:
    # create a set for cells visited
    # we have to use a depth first search since we can only explore each single side length without diverting from their parent node
    # add the perimeters in diff directions
    visit = set()
    def dfs(i,j):
        # base cases; out of bounds, less than zero or water
        if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]==0:
            return 1
        if (i,j) in visit:
            return 0
        
        visit.add((i,j))
        # adding the perimeters ; right, up, down and left side length
        perimeter = dfs(i,j+1)
        perimeter += dfs(i+1,j)
        perimeter += dfs(i-1,j)
        perimeter += dfs(i, j-1)
        return perimeter
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i,j)
        