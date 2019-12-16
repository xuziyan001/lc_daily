from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)
        if l1 == 0:
            if l2 % 2 == 0:
                return (nums2[l2//2] + nums2[l2//2-1]) / 2
            else:
                return nums2[l2//2]
        if l1 == 1:
            nums2 += nums1
            nums2.sort()
            return self.findMedianSortedArrays([], nums2)
        mid = (l1+l2) // 2
        i = l1 // 2
        j = mid - i
        a = 0.0
        while nums1[i-1] > nums2[j] or nums1[i] < nums2[j-1]:
            if nums1[i-1] > nums2[j]:
                i -= 1
                j += 1
            else:
                j -= 1
                i += 1
            if i <= 0:
                # 此时nums1全部为大值
                if (l1 + l2) % 2 == 0:
                    if mid == l2:
                        a = (nums1[0] + nums2[-1]) / 2
                    else:
                        a = (min(nums2[mid], nums1[0]) + nums2[mid-1]) / 2
                else:
                    a = min(nums1[0], nums2[mid])
                break
            if i >= l1:
                # 此时num1全部为小值
                if (l1 + l2) % 2 == 0:
                    if mid-l1 == 0:
                        a = (nums1[-1] + nums2[0]) / 2
                    else:
                        a = (max(nums1[-1], nums2[mid-l1-1]) + nums2[mid-l1]) / 2
                else:
                    a = nums2[mid-l1]
                break
        if a == 0:
            if (l1 + l2) % 2 == 0:
                a = (max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2
            else:
                a = min(nums1[i], nums2[j])
        return a


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,3,5,7,9], [2,4,6,8]),5)
    print(Solution().findMedianSortedArrays([1,3,5,7], [12,14,16,18,20]),12)
    print(Solution().findMedianSortedArrays([1,3,5,7,19], [12,14,16,18,20]),13)
    print(Solution().findMedianSortedArrays([], [12,14,16,18,20]),16)
    print(Solution().findMedianSortedArrays([], [12,14]),13)
    print(Solution().findMedianSortedArrays([], [12]),12)
    print(Solution().findMedianSortedArrays([1,2], [3,4]),2.5)
    print(Solution().findMedianSortedArrays([3,4], [1,2]),2.5)
    print(Solution().findMedianSortedArrays([4,5], [1,2,3]), 3)
    print(Solution().findMedianSortedArrays([1,2], [3,4,5]), 3)
    print(Solution().findMedianSortedArrays([3,4], [1,2,5]), 3)
    print(Solution().findMedianSortedArrays([1], [4]), 2.5)
    print(Solution().findMedianSortedArrays([1,3], [2,4,5,6]), 3.5)
    print(Solution().findMedianSortedArrays([1,2], [3,4,5,6,7]), 4)
