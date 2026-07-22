class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.value = nums[:]
        self.k = k
        
    def add(self, val: int) -> int:
        heapq.heappush(self.value, val)
        heapq.heapify(self.value)
        while len(self.value) > self.k:
            heapq.heappop(self.value)
        return self.value[0]
    
    
        

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)