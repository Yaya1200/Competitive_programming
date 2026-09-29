class Solution:

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        pacific = set()
        atlantic = set()
        output = []

        pacific_queue = deque()
        atlantic_queue = deque()

        rows = len(heights)
        cols = len(heights[0])

        
        for i in range(cols):
            pacific.add((0, i))
            pacific_queue.append((0, i))

   
        for j in range(rows):
            pacific.add((j, 0))
            pacific_queue.append((j, 0))

       
        while pacific_queue:

            r, c = pacific_queue.popleft()

            if r + 1 < rows:
                if heights[r][c] <= heights[r + 1][c] and (r + 1, c) not in pacific:
                    pacific.add((r + 1, c))
                    pacific_queue.append((r + 1, c))

            if r - 1 >= 0:
                if heights[r][c] <= heights[r - 1][c] and (r - 1, c) not in pacific:
                    pacific.add((r - 1, c))
                    pacific_queue.append((r - 1, c))

            if c + 1 < cols:
                if heights[r][c] <= heights[r][c + 1] and (r, c + 1) not in pacific:
                    pacific.add((r, c + 1))
                    pacific_queue.append((r, c + 1))

            if c - 1 >= 0:
                if heights[r][c] <= heights[r][c - 1] and (r, c - 1) not in pacific:
                    pacific.add((r, c - 1))
                    pacific_queue.append((r, c - 1))
        
        for i in range(cols):
                atlantic.add((rows - 1, i))
                atlantic_queue.append((rows - 1, i))

            
        for j in range(rows):
                atlantic.add((j, cols - 1))
                atlantic_queue.append((j, cols - 1))


        while atlantic_queue:

                r, c = atlantic_queue.popleft()

                if r + 1 < rows:
                    if heights[r][c] <= heights[r + 1][c] and (r + 1, c) not in atlantic:
                        atlantic.add((r + 1, c))
                        atlantic_queue.append((r + 1, c))

                if r - 1 >= 0:
                    if heights[r][c] <= heights[r - 1][c] and (r - 1, c) not in atlantic:
                        atlantic.add((r - 1, c))
                        atlantic_queue.append((r - 1, c))

                if c + 1 < cols:
                    if heights[r][c] <= heights[r][c + 1] and (r, c + 1) not in atlantic:
                        atlantic.add((r, c + 1))
                        atlantic_queue.append((r, c + 1))

                if c - 1 >= 0:
                    if heights[r][c] <= heights[r][c - 1] and (r, c - 1) not in atlantic:
                        atlantic.add((r, c - 1))
                        atlantic_queue.append((r, c - 1))
        for i in pacific:
            if i in atlantic:
                c,k = i
                output.append([c, k])
        return output
            
                    