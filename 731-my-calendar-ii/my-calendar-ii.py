class MyCalendarTwo:

    def __init__(self):
        self.value = []
        self.repeat = []

    def book(self, startTime: int, endTime: int) -> bool:

        for a, b in self.repeat:
            if startTime < b and endTime > a:
                return False

        value = []

        for i in self.value:
            a, b = i

            if startTime < b and endTime > a:
                value.append([max(startTime, a), min(endTime, b)])

        self.repeat.extend(value)
        self.value.append([startTime, endTime])

        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)