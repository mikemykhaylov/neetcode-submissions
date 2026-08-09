class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numlen = len(nums)
        l, r = 0, 1
        curr = nums[0]
        count = 1
        while r < numlen:
            if curr != nums[r]:
                l += 1
                nums[l] = curr = nums[r]
                count += 1

            r += 1

        return count