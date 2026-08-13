class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        output = []
        for i in strs:
            if str(sorted(i)) in hash_map:
                hash_map[str(sorted(i))].append(i)
            else:
                hash_map[str(sorted(i))] = [i]
        for i in hash_map:
            output.append(hash_map[i])
        return output        
        