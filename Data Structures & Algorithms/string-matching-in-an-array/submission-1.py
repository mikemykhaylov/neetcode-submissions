class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=lambda x:(len(x), x))
        print(words)
        currsubs, ressubs = set(), set()
        for word in words:
            confirmedsubs = []
            for currsub in currsubs:
                if currsub in word:
                    confirmedsubs.append(currsub)
            for confirmedsub in confirmedsubs:
                currsubs.remove(confirmedsub)
                ressubs.add(confirmedsub)
            currsubs.add(word)
        
        return list(ressubs)
