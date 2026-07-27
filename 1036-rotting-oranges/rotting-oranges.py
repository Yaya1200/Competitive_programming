class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i,j])
        proceded = 0
        result = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                i , j = queue.popleft()
                if j+1 < len(grid[i]) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    queue.append([i,j+1])
                if i+1 < len(grid) and  grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append([i+1,j])
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append([i-1,j])
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    queue.append([i,j-1])
            if queue:
                proceded +=1
            
        for row in grid:
            if 1 in row:
                return -1
        else:
            return proceded

            
        