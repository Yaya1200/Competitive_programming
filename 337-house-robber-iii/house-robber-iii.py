# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        graph = defaultdict(list)

        def build_graph(node):
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                build_graph(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                build_graph(node.right)

        build_graph(root)

        dp = {}

        def dfs(node, parent):
            skip = 0
            rob = node.val

            for child in graph[node]:
                if child == parent:
                    continue

                dfs(child, node)

                skip += max(dp[child][0], dp[child][1])

                rob += dp[child][0]

            dp[node] = (skip, rob)

        dfs(root, None)

        return max(dp[root])