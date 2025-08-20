class MinStack:

    def __init__(self):
        self.lst = []

    def push(self, val: int) -> None:
        if len(self.lst) == 0:
            self.lst.append(val)
            return None
        self.lst.append(val)


    def pop(self) -> None:
        self.lst.pop(len(self.lst)-1)

    def top(self) -> int:
        return self.lst[len(self.lst)-1]

    def getMin(self) -> int:
        return sorted(self.lst)[0]

minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-1);
minStack.getMin();
minStack.pop();
minStack.top();
minStack.getMin();