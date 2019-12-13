from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)
        res = 0
        return res


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,3,5,7,9], [2,4,6,8]))
    print(Solution().findMedianSortedArrays([1,3,5,7], [12,14,16,18,20]))
