class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.value = nums[:]
        self.k = k
        
    def add(self, val: int) -> int:
        self.value.append(val)
        self.value = sorted(self.value)
        return self.value[-self.k]
        

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)