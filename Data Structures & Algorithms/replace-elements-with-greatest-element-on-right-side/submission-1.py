class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        maxval = -1
        for i in range(len(arr) - 1, -1, -1):
            ans[i] = maxval
            maxval = max(arr[i], maxval)
        
        return ans