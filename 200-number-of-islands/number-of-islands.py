class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1":
                    total += 1

                    queue = deque()
                    queue.append((i, j))
                    grid[i][j] = "0"

                    while queue:
                        x, y = queue.popleft()

                        if x + 1 < rows and grid[x + 1][y] == "1":
                            grid[x + 1][y] = "0"
                            queue.append((x + 1, y))

              
                        if x - 1 >= 0 and grid[x - 1][y] == "1":
                            grid[x - 1][y] = "0"
                            queue.append((x - 1, y))

                     
                        if y + 1 < cols and grid[x][y + 1] == "1":
                            grid[x][y + 1] = "0"
                            queue.append((x, y + 1))

                    
                        if y - 1 >= 0 and grid[x][y - 1] == "1":
                            grid[x][y - 1] = "0"
                            queue.append((x, y - 1))

        return total