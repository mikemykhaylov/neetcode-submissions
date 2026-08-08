class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        out = ""

        while i < len(word1) and i < len(word2):
            out += word1[i] + word2[i]
            i += 1
        
        if i < len(word1):
            out += word1[i:]
        else:
            out += word2[i:]

        return out