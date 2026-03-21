class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map = {}
        output = []
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        for i in hash_map:
            output.append(hash_map[i])
        for i in range(len(output)):
            for j in range(len(output)-i-1):
                if output[j] > output[j+1]:
                    output[j], output[j+1] = output[j+1], output[j]

        for i in output:
            for j in hash_map:
                if i == hash_map[j] and j not in result:
                    result += [j] * i
                    break
        return result


        
        