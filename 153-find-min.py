"""
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。
例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        start = 0
        end = n - 1
        mid = (start + end) // 2
        while end > mid > start:
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                if nums[mid] > nums[end]:
                    start = mid+1
                else:
                    end = mid
            else:
                return min(nums[mid], nums[mid+1])
            mid = (start+end) // 2
        return min(nums[start], nums[end])


if __name__ == '__main__':
    l = [4,5,6,7,0,1,2]
    print(Solution().findMin(l))
    l = [11,13,15,17]
    print(Solution().findMin(l))
    l = [3,4,5,1,2]
    print(Solution().findMin(l))
    l = [2,3,4,5,1]
    print(Solution().findMin(l))
