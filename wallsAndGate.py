def wallsAndGate(self, rooms: List[List[int]]) -> int:
    visit = set()
    rows, col = len(rooms), len(rooms[0])
    dis = 0
    # function fills an empty/ add room
    q = deque()
    
    def addRooms(r,c):
        if (r<0 or c<0 or r==rows or c == col or rooms[r][c] == -1 or (r,c) in visit):
            return
        visit.add((r,c))
        q.append([r,c])
    
    for r in range(rows):
        for c in range(col):
            if rooms[r][c] == 0:
                q.append([r,c])
                visit.add((r,c))
    
    while q:
        for i in range(len(q)):
             r,c = q.popleft()
             rooms[r][c] = dis
             addRooms(r,c+1)
             addRooms(r+1,c)
             addRooms(r-1,c)
             addRooms(r,c-1)
        dis +=1
