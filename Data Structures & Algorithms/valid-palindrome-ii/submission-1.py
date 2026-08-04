class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        removed = False
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            removed = True
            break
        
        if not removed:
            return True

        prevl, prevr = l, r
        idx = (0, 0)
        if s[l + 1] == s[r]:
            idx = (0, -1)
            l += 1
        elif s[l] == s[r - 1]:
            idx = (1, 0)
            r -= 1
        else:
            return False

        match = True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            match = False
            break

        if match:
            return True

        l, r = prevl + idx[0], prevr + idx[1]

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            return False

        return True
            