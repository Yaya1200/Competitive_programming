class MyCalendar:

    def __init__(self):
        self.value = []

    def book(self, startTime: int, endTime: int) -> bool:
        for f,l in self.value:
            if not(startTime >= l or endTime<= f ):
                return False
        self.value.append([startTime, endTime])
        return True

        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)