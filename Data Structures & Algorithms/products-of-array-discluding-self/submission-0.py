class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)

        pre_mult = 1
        for i in range(len(nums) - 1):
            pre_mult *= nums[i]
            out[i + 1] *= pre_mult

        post_mult = 1
        for i in range(len(nums) - 1, 0, -1):
            post_mult *= nums[i]
            out[i-1] *= post_mult

        return out