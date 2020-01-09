from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return target == nums[0]
        start, end = 0, len(nums)-1
        mid = (end+start) // 2
        if nums[start] > nums[mid]:
            if nums[mid] < target <= nums[end]:
                return self.search(nums[mid+1:], target)
            else:
                return self.search(nums[:mid+1], target)
        elif nums[start] < nums[mid]:
            if nums[start] <= target < nums[mid]:
                return self.search(nums[:mid], target)
            else:
                return self.search(nums[mid:], target)
        else:
            current = nums[start]
            if current == target:
                return True
            while start < end and nums[start] == current:
                start += 1
            return self.search(nums[start:], target)


if __name__ == '__main__':
    l = [2,5,6,0,0,1,2]
    print(Solution().search(l, 0))
    print(Solution().search(l, 3))
    l = [2] * 655
    print(Solution().search(l, 3))
