class MyCalendar:

    def __init__(self):
        self.data = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.data:
            if not (endTime <= s or startTime >= e):
                return False

        self.data.append((startTime, endTime))
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)