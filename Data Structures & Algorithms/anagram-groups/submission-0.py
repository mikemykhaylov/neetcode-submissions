from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)

        for anag in strs:
            count = Counter(anag)
            key = [0] * 26
            for char in count.keys():
                key[ord(char) - ord('a')] = count[char]
            
            keystr = ','.join(str(keyint) for keyint in key)
            out[keystr].append(anag)

        return [val for val in out.values()]