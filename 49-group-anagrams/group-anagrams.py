class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        output = []
        for i in strs:
            if str(sorted(i)) not in hash_map:
                hash_map[str(sorted(i))] = []
            hash_map[str(sorted(i))].append(i)
                  
        for i in hash_map:
            output.append(hash_map[i])
        return output        
        