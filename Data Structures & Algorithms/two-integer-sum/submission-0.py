class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = {}
        for i, num in enumerate(nums):
            if target - num in rec:
                return [rec[target - num], i]
            rec[num] = i