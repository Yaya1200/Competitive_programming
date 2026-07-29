class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        queue.append(0)
        visited.add(0)
        while queue:
            node = queue.popleft()
            for neb in rooms[node]:
                if neb in visited:
                    continue
                queue.append(neb)
                visited.add(neb)
        return len(rooms) == len(visited)

            