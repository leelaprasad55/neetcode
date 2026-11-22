class MinStack:

    def __init__(self):
        self.st=[]
        self.ms=[]
    def push(self, val: int) -> None:
        self.st.append(val)
        mv=min(val,self.ms[-1] if self.ms else val)
        self.ms.append(mv)
    def pop(self) -> None:
        self.ms.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.ms[-1]
        
