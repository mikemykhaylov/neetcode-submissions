class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = count = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                count += 1
                i += 1

        return count