class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        values = []
        hash_map = {}
        for i in range(len(senders)):
            if senders[i] in hash_map:
                hash_map[senders[i]] += " " + messages[i]
            else:
                hash_map[senders[i]] = messages[i]
        
        for i in hash_map:
            hash_map[i] = hash_map[i].count(" ")+1
        for i in hash_map:
            values.append([hash_map[i], i])
        print(values)
        heapq.heapify(values)
        while len(values) > 1:
              heapq.heappop(values)
        return values[0][1]

