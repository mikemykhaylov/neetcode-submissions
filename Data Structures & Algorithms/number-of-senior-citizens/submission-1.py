class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for id in details:
            if id[11] in ['7','8','9'] or (id[11] == '6' and id[12] != '0'):
                res += 1

        return res