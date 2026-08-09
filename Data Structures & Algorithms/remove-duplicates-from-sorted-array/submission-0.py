class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numlen = len(nums)
        l, r = 0, 0
        curr = None
        count = 0
        while r < numlen:
            # print(l, r, nums)
            if curr == None:
                curr = nums[r]
                count += 1
                r += 1
                continue
            
            if curr != nums[r]:
                l += 1
                nums[l] = curr = nums[r]
                count += 1

            r += 1

        return count