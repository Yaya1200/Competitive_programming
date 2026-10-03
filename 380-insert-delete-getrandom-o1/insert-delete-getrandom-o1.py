class RandomizedSet:

    def __init__(self):
        self.value = set()

    def insert(self, val: int) -> bool:
        if val not in self.value:
            self.value.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.value:
            self.value.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        num = len(self.value)
        value1 = random.randint(0, num-1)
        return list(self.value)[value1]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()