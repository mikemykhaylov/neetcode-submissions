class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = freespace = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
                continue
            leftfree = i == 0 or flowerbed[i-1] == 0
            rightfree = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            if leftfree and rightfree and flowerbed[i] == 0:
                freespace += 1
                i += 1
            i += 1
            
        return freespace >= n