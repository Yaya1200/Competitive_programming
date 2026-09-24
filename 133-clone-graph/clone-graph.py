from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash_map = {}
        queue = deque()

        if node:
            queue.append(node)

        while queue:
            value = queue.popleft()

            if value.val not in hash_map:
                hash_map[value.val] = []

                for i in value.neighbors:
                    hash_map[value.val].append(i.val)

                    if i.val not in hash_map:
                        queue.append(i)

        nodes = {}

        for i in hash_map:
            nodes[i] = Node(i)

        for i in hash_map:
            for neighbor in hash_map[i]:
                nodes[i].neighbors.append(nodes[neighbor])
        

        return nodes[node.val] if node else None