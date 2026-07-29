class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        inital_color = image[sr][sc]
        queue = deque()
        queue.append([sr,sc])
        image[sr][sc] = color
        if inital_color == color:
              return image
        while queue:
          r,c = queue.popleft()
          if r+1 < len(image) and image[r+1][c] == inital_color:
            queue.append([r+1,c])
            image[r+1][c] = color
          if r-1 >= 0 and image[r-1][c] == inital_color:
            queue.append([r-1,c])
            image[r-1][c] = color
          if c- 1 >= 0 and image[r][c-1] == inital_color:
            queue.append([r,c-1])
            image[r][c-1] = color
          if c+1 < len(image[r]) and image[r][c+1] == inital_color:
            queue.append([r,c+1])
            image[r][c+1] = color
        return image
          

        