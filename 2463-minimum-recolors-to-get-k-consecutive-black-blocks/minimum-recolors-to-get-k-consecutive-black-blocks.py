class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        result = float('inf')
        for i in range(len(blocks)-k+1):
            value = blocks[i:i+k]
            count = value.count('W')
            result = min(count, result)
            count = 0
        return result

        