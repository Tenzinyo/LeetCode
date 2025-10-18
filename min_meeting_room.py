def min_meeting_room(self,interval):
    n = len(interval)
    start = sorted([i.start for i in interval])
    end = sorted([i.end for i in interval])
    res,count = 0,0
    s,e = 0,0
    while s<len(n):
        if start[s]<end[e]:
            s+=1
            count+=1
        else:
            e+=1
            count-=1
        res = max(res,count)
    return res