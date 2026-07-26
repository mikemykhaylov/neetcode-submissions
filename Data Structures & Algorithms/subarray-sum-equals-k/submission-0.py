class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out = 0
        prefixes = {}

        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum == k:
                out += 1
            
            if curr_sum - k in prefixes:
                out += prefixes[curr_sum - k]
            
            prefixes[curr_sum] = 1 if curr_sum not in prefixes else prefixes[curr_sum] + 1

        return out