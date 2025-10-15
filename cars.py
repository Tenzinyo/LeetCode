def carsPassing(n):
    countZero = 0
    countCars = 0
    for i in range(len(n)):
        # traverse from the left to right, west to east
        if n[i] == 0:       
            countZero+=1
        else:
            countCars+=countZero
        i+=1
    return countCars
