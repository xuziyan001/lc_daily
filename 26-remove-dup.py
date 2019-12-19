from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i, j = 0, 1
        tmp = nums[0]
        i += 1
        while j < len(nums):
            if nums[j] == tmp:
                j += 1
            else:
                tmp = nums[j]
                nums[i] = tmp
                i += 1
                j += 1
        return i


if __name__ == '__main__':
    l = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(l))
    print(l)
