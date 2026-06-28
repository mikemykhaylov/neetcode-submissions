class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for id in details:
            if int(id[11:13]) > 60:
                res += 1

        return res