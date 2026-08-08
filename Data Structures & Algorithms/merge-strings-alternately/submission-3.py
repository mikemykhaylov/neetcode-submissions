class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        i = 0
        out = [''] * (len1 + len2)

        while i < len1 and i < len2:
            out[2 * i], out[2 * i + 1] = word1[i], word2[i]
            i += 1
        
        if i < len1:
            out[2*i:] = word1[i:]
        else:
            out[2*i:] = word2[i:]

        return ''.join(out)