class Solution:
    def canJump(self, nums: List[int]) -> bool:
        queue = deque()
        visited = set()

        queue.append([nums[0], 0])
        visited.add(0)

        while queue:
            value, index = queue.popleft()

            for i in range(index+1, min(index + value + 1, len(nums))):
                if i == len(nums)-1:
                    return True

                if i not in visited:
                    queue.append([nums[i], i])
                    visited.add(i)

        return len(nums) == 1