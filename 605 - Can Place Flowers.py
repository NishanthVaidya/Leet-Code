class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                left = 0 if i == 0 else flowerbed[i - 1]
                right = 0 if i == length - 1 else flowerbed[i + 1]
                if left == 0 and right == 0:
                    flowerbed[i] = 1 
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0
