class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        checked = set()
        out = []

        for i, num in enumerate(nums):
            if num in checked or num > 1:
                continue
            target = 0 - num

            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    out.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

            checked.add(num)
        
        return out