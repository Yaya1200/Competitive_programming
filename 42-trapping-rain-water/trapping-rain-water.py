class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        output = 0

        for i in range(len(height)):
            if not stack:
                stack.append(i)

            else:
                if height[stack[-1]] > height[i]:
                    stack.append(i)

                else:
                    while stack and height[i] > height[stack[-1]]:
                        bottom = stack.pop()

                        if not stack:
                            break

                        left = stack[-1]

                        width = i - left - 1
                        result = min(height[left], height[i]) - height[bottom]

                        result = result * width
                        output += result
                      

                    stack.append(i)

        return output
        