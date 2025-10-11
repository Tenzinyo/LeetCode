def oasis(land,gas):
    result = False
    steps = 0
    
    def dfs(land,i,j,gas,steps):
        if (i<0 or j<0 or i>len(land) or j>len(land) or steps>gas or land[i][j]==0):
            return False
        count = dfs(land, i+1,j,gas,steps)
        count = dfs(land, i-1,j,gas,steps)
        count = dfs(land, i,j+1,gas,steps)
        count = dfs(land, i,j-1,gas,steps)
        if land[i][j]=="o":
            return True
        
        return count
    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j]=="c":
                steps+=1
                result = dfs(land,i,j,gas,steps)
    return result
    
        
        
        