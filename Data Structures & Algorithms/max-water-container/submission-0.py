class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = 0

        l, r = 0, len(heights) - 1
        while l < r:
            out = max(out, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return out