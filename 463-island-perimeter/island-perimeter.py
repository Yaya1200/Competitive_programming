class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        value = []
        perimeter = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    value = [i, j]
                    break
            if value:
                break

        queue = deque()
        queue.append(value)
        visited.add((value[0], value[1]))

        while queue:
            i, j = queue.popleft()
            perimeter += 4
            if i + 1 < len(grid) and grid[i+1][j] == 1:
                perimeter -= 1
                if (i+1, j) not in visited:
                    visited.add((i+1, j))
                    queue.append([i+1, j])
            if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
                perimeter -= 1
                if (i, j+1) not in visited:
                    visited.add((i, j+1))
                    queue.append([i, j+1])

            if i - 1 >= 0 and grid[i-1][j] == 1:
                perimeter -= 1
                if (i-1, j) not in visited:
                    visited.add((i-1, j))
                    queue.append([i-1, j])

            if j - 1 >= 0 and grid[i][j-1] == 1:
                perimeter -= 1
                if (i, j-1) not in visited:
                    visited.add((i, j-1))
                    queue.append([i, j-1])

        return perimeter