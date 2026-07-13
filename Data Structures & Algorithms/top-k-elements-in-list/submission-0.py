from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]
        count = Counter(nums)
        for val, valcount in count.items():
            buckets[valcount - 1].append(val)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i]) - 1, -1, -1):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res