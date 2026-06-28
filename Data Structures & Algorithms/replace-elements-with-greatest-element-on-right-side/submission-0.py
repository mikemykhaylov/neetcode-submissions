class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = arr
        maxval = res[n - 1]
        res[n - 1] = -1
        for i in range(len(arr) - 2, -1, -1):
            val = res[i]
            res[i] = maxval
            maxval = max(val, maxval)
        
        return res