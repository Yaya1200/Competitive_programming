class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in strs:
            if str(sorted(i)) not in hash_map:
                hash_map[str(sorted(i))] = []
            hash_map[str(sorted(i))].append(i)   
              
        return list(hash_map.values())        
        