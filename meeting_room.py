class MR(object):
    def __init__(self, start,end):
        self.start = start
        self.end= end
def meeting(self,intervals):
    n = len(intervals)
    intervals.sort(key = lambda i:i.start)
    for i in range(1,n):
        i1 = intervals[i-1]
        i2 = intervals[i]
        if i1.end> i2.start:
            return False
    return True
        
        