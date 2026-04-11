class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        output = []
        hash_map = []
        for i in nums:
            if i < pivot:
                hash_map.append([i, -1])
            elif i > pivot:
                hash_map.append([i, 1])
            else:
                hash_map.append([i, 0])
        for i in hash_map:
            if i[1] == -1:
                output.append(i[0])
        for i in hash_map:
            if i[1] == 0:
                output.append(i[0])
        for i in hash_map:
            if i[1] == 1:
                output.append(i[0])
        return output