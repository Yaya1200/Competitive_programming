# Definition for a binary tree node:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distanceK(self, root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:

        parent = {}

        def dfs(node, par=None):
            if not node:
                return

            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

     
        queue = deque([(target, 0)])
        visited = {target}

        while queue:
            node, dist = queue.popleft()

            if dist == k:
                result = [node.val]
                result.extend(n.val for n, d in queue if d == k)
                return result

            for neighbor in (
                node.left,
                node.right,
                parent[node]
            ):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return []
