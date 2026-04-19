class MinStack:

    def __init__(self):
        self.value = []
    def push(self, val: int) -> None:
        self.value.append(val)
    def pop(self) -> None:
        self.value.pop()
    def top(self) -> int:
        return self.value[-1]       
    def getMin(self) -> int:
        min_value = self.value[0]
        for i in range(1, len(self.value)):
            min_value = min(min_value, self.value[i])
        return min_value



        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()