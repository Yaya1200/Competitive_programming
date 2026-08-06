class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[0] == 0 and flowerbed[1] == 0:
                n -= 1
                flowerbed[i] = 1
            elif i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[-2] == 0:
                n-=1
                flowerbed[i] = 1
            else:
                if i > 0 and i < len(flowerbed)-1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
            if n == 0:
                return True
        return False


