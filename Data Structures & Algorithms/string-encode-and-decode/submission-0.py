class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        out += f"{len(strs)}:"
        for list_str in strs:
            out += f"{len(list_str)}:{list_str}"
        return out

    def decode(self, s: str) -> List[str]:
        list_len_str = s.split(":")[0]
        out = []

        # i now at first char of word length
        i = len(list_len_str) + 1

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


