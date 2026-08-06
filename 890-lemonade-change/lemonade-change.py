class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hash_map = {5:0, 10:0, 20:0}
        for i in bills:
            hash_map[i] += 1
            value = i - 5
            while value > 0 :
                if value >= 10 and hash_map[10] > 0:
                    hash_map[10] -= 1
                    value -= 10
                elif value >= 5 and hash_map[5] > 0:
                    hash_map[5] -= 1
                    value -= 5
                else:
                    break
            if value > 0:
                return False
        return True

