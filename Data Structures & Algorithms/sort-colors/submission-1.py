from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        r, g, b = count[0], count[1], count[2]
        print(r, g, b)
        for i in range(r):
            nums[i] = 0
        for j in range(r, r + g):
            nums[j] = 1
        for k in range (r + g, r + g + b):
            nums[k] = 2

        