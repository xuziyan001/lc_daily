from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        start = 0
        end = l-1
        while end >= start:
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                # left is longer
                if target > nums[mid]:
                    start = mid + 1
                elif nums[start] < target < nums[mid]:
                    end = mid - 1
                elif target < nums[mid] and nums[start] > target:
                    start = mid + 1
                else:
                    return start if nums[start] == target else mid
            elif nums[mid] < nums[start]:
                # right is longer
                if target < nums[mid]:
                    end = mid - 1
                elif nums[mid] < target < nums[end]:
                    start = mid + 1
                elif nums[mid] < target and nums[end] < target:
                    end = mid - 1
                else:
                    return end if nums[end] == target else mid
            else:
                if nums[mid] == target:
                    return mid
                if nums[end] == target:
                    return end
                else:
                    return -1
        return -1


if __name__ == '__main__':
    print(Solution().search([4,5,6,7,0,1,2], 4))
    print(Solution().search([4,5,6,7,0,1,2], 3))
    print(Solution().search([4,5,6,7,0,1,2], 0))
    print(Solution().search([1,3], 3))
