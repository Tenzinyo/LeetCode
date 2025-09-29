import random
def __init__(self):
    self.numMap = {}
    self.numList = []
    
def insert(val):
    res = val not in self.numMap
    if res:
        self.numMap[val] = len(self.numList)
        self.numList.append(val)
    return res

def remove(val):
    res = val in self.numMap
    if not res:
        index = self.numMap[val]
        lastIndex = self.numList[-1]
        self.numList[index] = lastIndex
        self.numList.pop()
        self.numMap[lastIndex] = index
        del self.numMap[val]
    return res

def getRandom(val):
    return random.choice(self.numList)
    