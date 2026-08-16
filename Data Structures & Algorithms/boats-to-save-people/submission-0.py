class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        out = 0
        people.sort()

        l, r = 0, len(people) - 1

        while l <= r:
            heavy = people[r]
            leftover = limit - heavy
            out += 1
            r -= 1
            if people[l] <= leftover:
                l += 1

        return out
