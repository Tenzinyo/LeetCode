def count(arr):
    count0 = 0
    countcars = 0
    # [0,1,0,1,1]
    # count0 = 2
    # countcar = 3
    for i in range(len(arr)):
        if arr[i]==0:
            count0+=1
        else:
            countcars+=count0
    return countcars