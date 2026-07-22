class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) > 1:
            for i in range(len(stones)):
               stones[i] = -stones[i]
            while len(stones) > 1:
                heapq.heapify(stones)
                stone1 = -heapq.heappop(stones)
                heapq.heapify(stones)
                stone2 = -heapq.heappop(stones)
                if stone1 != stone2:
                    heapq.heappush(stones,stone2-stone1)
        else:
            return stones[0]
        if stones:
            return -stones[0]
        else:
            return 0
            
          
      

        
        

        