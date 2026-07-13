class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sortInternal(nums, 0, len(nums))
        return nums

    def sortInternal(self, nums: List[int], start: int, end: int):
        if end - start < 2:
            return

        mid = (start + end) // 2
        nums[mid], nums[end - 1] = nums[end - 1], nums[mid]
        
        i = pivotidx = start
        pivot = nums[end - 1]
        while i < end - 1:
            val = nums[i]
            if val >= pivot:
                i += 1
            else:
                if i != pivotidx:
                    nums[i], nums[pivotidx] = nums[pivotidx], nums[i]
                i += 1
                pivotidx += 1

        nums[i], nums[pivotidx] = nums[pivotidx], nums[i]
        self.sortInternal(nums, start, pivotidx)
        self.sortInternal(nums, pivotidx + 1, end)
        return
        
