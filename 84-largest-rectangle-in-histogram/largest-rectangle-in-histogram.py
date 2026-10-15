
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        result = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                result = max(result, h * width)

            stack.append(i)

        heights.pop()
        return result

