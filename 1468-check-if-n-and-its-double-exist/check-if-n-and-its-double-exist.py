class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_map = {}
        for i in range(len(arr)):
            if arr[i]*2 in arr[:i] or arr[i]*2 in arr[i+1:]:
                hash_map[i] = 2
            else:
                hash_map[i] = 1
        for i in hash_map:
            if hash_map[i] == 2:
                return True
        return False
            


            