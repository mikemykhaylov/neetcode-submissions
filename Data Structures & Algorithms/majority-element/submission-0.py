class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = nums[0]
        count = maxcount = 1
        for i in range(len(nums)):
            num = nums[i]
            if num == elem:
                count += 1
                continue
            count -= 1
            if count == 0:
                elem = num
                count += 1
        
        return elem
