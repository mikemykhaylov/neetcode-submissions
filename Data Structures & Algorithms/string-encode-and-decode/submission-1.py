class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for list_str in strs:
            out += f"{len(list_str)}:{list_str}"
        return out

    def decode(self, s: str) -> List[str]:
        i = 0
        out = []

        # loop that collects by word
        while i < len(s):
            word_len_str = ""
            # collect following str len
            while s[i] != ":":
                word_len_str += s[i]
                i += 1
            
            # i now at :
            word_len = int(word_len_str)

            # i now at first char of word
            i += 1
            out.append(s[i:i + word_len])

            # i now at first char of word length
            i = i + word_len

        return out


