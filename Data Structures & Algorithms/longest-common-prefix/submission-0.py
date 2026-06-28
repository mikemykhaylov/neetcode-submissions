class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pfx = strs[0]
        for string in strs:
            n = len(pfx) - 1
            for i in range(n, -1, -1):
                if i < len(string) and pfx[i] == string[i]:
                    continue
                pfx = pfx[:i]

        return pfx