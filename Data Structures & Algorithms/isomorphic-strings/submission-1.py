from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        mapping = dict()
        maprange = set()
        for i in range(n):
            sc, tc = s[i], t[i]
            if sc in mapping and mapping[sc] == tc:
                continue
            elif sc in mapping or tc in maprange:
                return False
            else:
                mapping[sc] = tc
                maprange.add(tc)

        return True
            
