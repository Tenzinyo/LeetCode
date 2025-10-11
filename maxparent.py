def maxDepth(s):
    counter = 0
    res = 0
    for i in s:
        if (i=="("):
            counter+=1
        elif (i==")"):
            counter-=1
        res = max(res,counter)
    return res