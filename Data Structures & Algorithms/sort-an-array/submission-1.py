class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        stack = [[0, len(nums)]]

        while len(stack) > 0:
            val = stack.pop()
            stack += self.sortInternal(nums, val[0], val[1])

        return nums

    def sortInternal(self, nums: List[int], start: int, end: int) -> List[List[int]]:
        if start == end:
            return []
        
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
        return [[start, pivotidx], [pivotidx + 1, end]]
        
