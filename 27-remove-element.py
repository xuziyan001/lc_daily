from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i, j = 0, 0
        while i < len(nums) and nums[i] != val:
            i += 1
        if i == len(nums):
            return len(nums)
        j = i+1
        if j == len(nums):
            return len(nums)-1
        while j < len(nums):
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                j += 1
                i += 1
        return i


if __name__ == '__main__':
    l = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(l, val))
    print(l)
    l = [2]
    val = 2
    print(Solution().removeElement(l, val))
    print(l)
