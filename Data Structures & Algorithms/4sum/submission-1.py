class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        checked = set()
        out = []

        for i, num in enumerate(nums):
            if num in checked:
                continue
            left = target - num

            l, r = i + 1, len(nums) - 1
            # print(left, l, r)

            while l < r:
                if nums[l] + nums[r] == left:
                    out.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                elif nums[l] + nums[r] > left:
                    r -= 1
                else:
                    l += 1

            checked.add(num)
        
        return out
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        checked = set()
        out = []

        for i, num in enumerate(nums):
            if num in checked:
                continue
            left = target - num
            # print(nums[i + 1:], left)

            threesum = self.threeSum(nums[i + 1:], left)
            for triple in threesum:
                out.append([num, *triple])

            checked.add(num)
        
        return out
        