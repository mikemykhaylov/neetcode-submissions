class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k % n == 0:
            return 0

        for i in range(n):
            nums[i] += 2**31

        for i in range(k % n):
            if nums[i] < 0:
                continue

            curr = i
            temp = nums[curr]
            while True:
                curr = (curr + k) % n
                nums[curr], temp = temp * -1, nums[curr]
                if curr == i:
                    break
        
        for i in range(n):
            nums[i] *= -1
            nums[i] -= 2**31