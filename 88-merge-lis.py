from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(len(nums1))
        nums1[m:] = nums2[:n]
        print(len(nums1))
        nums1.sort()


if __name__ == '__main__':
    l = [1,2,3,0,0,0,0,0]
    r = [2,5,6]
    print(Solution().merge(l,3,r,3))
    print(l)


