from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        min_count = len(nums) // 3

        leaders = 0
        counts = defaultdict(int)

        for num in nums:
            if num in counts:
                counts[num] += 1
            elif leaders < 2:
                counts[num] += 1
                leaders += 1
            else:
                # leader_removed = False
                for key in [key for key in counts.keys()]:
                    counts[key] -= 1
                    if counts[key] == 0:
                        del counts[key]
                        leaders -= 1
                        # leader_removed = True
                        # break
                # counts[num] += 1
                # if leader_removed:
                #     leaders += 1


        out = []
        for key in counts.keys():
            key_count = 0
            for num in nums:
                if num == key:
                   key_count += 1
            if key_count > min_count:
                out.append(key)
        
        return out


