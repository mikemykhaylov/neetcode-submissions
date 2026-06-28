class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentones = maxones = i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == 1:
                currentones += 1
                i += 1
            maxones = max(maxones, currentones)
            currentones = 0
            i += 1

        return maxones