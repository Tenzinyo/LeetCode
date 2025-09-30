class RandomizedCollection(object):

    def __init__(self):
        self.maps = {}
        self.lst = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val not in self.maps
        if not res:
            self.maps[val] = len(self.lst)
            self.lst.append(val)
        else:
            self.maps[val] = len(self.lst)
            self.lst.append(val)
        return res

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val in self.maps
        if res:
            index = self.maps[val]
            last_index = self.lst[-1]
            self.lst[index] = last_index
            self.lst.pop()
            self.maps[last_index] = index
            del self.maps[val]
        return res

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.lst)
        