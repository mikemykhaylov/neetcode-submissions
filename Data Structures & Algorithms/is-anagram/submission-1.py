from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = defaultdict(int)
        for c in s:
            count1[c]+=1
        for c in t:
            count1[c]-=1
        for count in count1.values():
            if count != 0:
                return False

        return True