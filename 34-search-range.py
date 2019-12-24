from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        t = -1
        while end >= start:
            mid = (start+end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                t = mid
                break
        if t == -1:
            return [-1, -1]
        start, end = t, t
        while start >= 0:
            if nums[start] == target:
                start -= 1
            else:
                start += 1
                break
        if start < 0:
            start = 0
        while end <= len(nums)-1:
            if nums[end] == target:
                end += 1
            else:
                end -= 1
                break
        if end == len(nums):
            end -= 1
        return [start, end]


if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10], 8))
    print(Solution().searchRange([5,7,7,8,8,10], 6))
    print(Solution().searchRange([5,7,7,8,8,10], 10))
    print(Solution().searchRange([5,7,7,8,8,10], 5))
    print(Solution().searchRange([1], 1))
    print(Solution().searchRange([1,4], 4))
