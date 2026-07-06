def cleanmail(email: str) -> str:
    local, domain = email.split("@")
    local = local.split('+')[0]
    local = ''.join([c for c in local if c != '.'])
    return "@".join([local, domain])

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        out = set()
        for email in emails:
            clean = cleanmail(email)
            print(clean, email)
            out.add(clean)

        return len(out)