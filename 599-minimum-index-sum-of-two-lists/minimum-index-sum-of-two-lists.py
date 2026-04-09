class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = {}
        output = []
        result = []
        min_value = float('inf')
        for i in range(len(list1)):
            hash_map[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in hash_map:
                output.append([list2[j], j+hash_map[list2[j]]])
                min_value = min(min_value, j+hash_map[list2[j]])
        for i in output:
            if i[1] == min_value:
                result.append(i[0])
        return result
        