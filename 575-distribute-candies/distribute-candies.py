class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        value = len(candyType)//2
        candyType = len(set(candyType))
        if candyType < value:
            return candyType
        else:
            return value
        