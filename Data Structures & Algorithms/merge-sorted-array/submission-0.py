class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i, num in enumerate(nums2):
            l, r = 0, m + i

            while l < r:
                mid = (l + r) // 2
                midnum = nums1[mid]
                if midnum == num:
                    break
                elif midnum > num:
                    r = mid
                else:
                    l = mid + 1
                
            numpos = (l + r) // 2
            # print(nums1, num, numpos)

            nextnum = num
            while numpos < m + i + 1:
                nums1[numpos], nextnum = nextnum, nums1[numpos]
                numpos += 1

            # print(nums1)

                

        