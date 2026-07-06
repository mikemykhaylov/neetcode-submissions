from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maxodd = -1
        mineven = len(s)
        for val in c.values():
            if val & 1 == 1:
                maxodd = max(maxodd, val)
            else:
                mineven = min(mineven, val)

        return maxodd - mineven