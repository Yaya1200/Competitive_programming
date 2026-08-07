class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque([0])
        visited = set([0])
        jumps = 0

        while queue:
            size = len(queue)

            for i in range(size):
                index = queue.popleft()

                if index == len(nums)-1:
                    return jumps

                for next_index in range(index + 1, min(index + nums[index] + 1, len(nums))):
                    if next_index not in visited:
                        visited.add(next_index)
                        queue.append(next_index)

            jumps += 1

 


             
            
        