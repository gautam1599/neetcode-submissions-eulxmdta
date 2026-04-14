class MinStack:

    def __init__(self):
        self.res=[]
        

    def push(self, val: int) -> None:
        self.res.append(val)

    def pop(self) -> None:
        self.res.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        tmp=[]
        mini=self.res[-1]

        while len(self.res):
            mini=min(mini,self.res[-1])
            tmp.append(self.res.pop())
        while len(tmp):
            self.res.append(tmp.pop())
        return mini
