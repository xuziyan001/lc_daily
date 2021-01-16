"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
"""

"""
从后往前遍历，确认插入元素的位置
"""

from typing import List


class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(len(nums1))
        nums1[m:] = nums2[:n]
        print(len(nums1))
        nums1.sort()

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 这里
        i = m-1
        j = n-1
        insert = m+n-1
        while insert >= 0 and i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[insert] = nums1[i]
                i -= 1
                insert -= 1
            else:
                nums1[insert] = nums2[j]
                j -= 1
                insert -= 1
        if i < 0:
            nums1[:j] = nums2[:j]


if __name__ == '__main__':
    l = [1,2,3,0,0,0,0,0]
    r = [2,5,6]
    print(Solution().merge(l,3,r,3))
    print(l)
    l = [0]
    r = [1]
    print(Solution().merge(l,0,r,1))
    print(l)



