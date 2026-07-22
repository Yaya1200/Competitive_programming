class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        values = []
        hash_map = {}
        output = []
        for i in words:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        for i in hash_map:
            values.append([-hash_map[i], i])
        i = 0
        while i < k:
            heapq.heapify(values)
            output.append(values[0][1])
            heapq.heappop(values)
            i+= 1
        return output

        