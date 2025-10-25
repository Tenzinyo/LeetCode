class OrderedStream():
    def __init__(self,n) -> None:
        self.lst = [None]*n
        self.pointer = 0
    def insert(self,id,v):
        self.lst[id-1] = v
        sp = self.pointer
        while self.pointer<len(self.lst) and self.lst[self.pointer]:
            self.pointer+=1
        return self.lst[sp:self.pointer]
    