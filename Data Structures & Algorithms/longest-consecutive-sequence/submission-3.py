class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        union_find = {}
        max_val = min(1, len(nums))

        for num in nums:
            # print(num)
            num += 10 ** 9
            if num in union_find:
                # print(f"{num} already seen")
                continue

            union_find[num] = -1

            if num + 1 in union_find:
                # print(f"{num} has successor")
                union_find[num] = union_find[num + 1] - 1
                union_find[num + 1] = num
                # print(union_find[num], union_find[num + 1])
                max_val = max(max_val, union_find[num] * -1)

            if num - 1 in union_find:
                # print(f"{num} has predecessor")
                idx = num - 1

                while idx >= 0 and union_find[idx] >= 0:
                    idx = union_find[idx]
                
                # print(f"Start of sequence is {idx}")
                # idx is at the start of the sequence
                union_find[idx] += union_find[num]
                max_val = max(max_val, union_find[idx] * -1)
                union_find[num] = idx
                # print(union_find[idx], union_find[num])

                
        return max_val
        