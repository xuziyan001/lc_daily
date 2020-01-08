from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return None
        i = 0
        j = len(nums)-1
        while i <= j and nums[i] == 0:
            i += 1
        if i >= j:
            return None
        while j >= 0 and nums[j] == 2:
            j -= 1
        if j <= 0:
            return None
        cur = i
        while cur != j+1:
            if nums[cur] == 0:
                nums[cur], nums[i] = nums[i], nums[cur]
                i += 1
                cur = i
            elif nums[cur] == 2:
                nums[cur], nums[j] = nums[j], nums[cur]
                j -= 1
            else:
                cur += 1


if __name__ == '__main__':
    l = [2,0,2,1,1,0]
    Solution().sortColors(l)
    print(l)
    l = [2, 0, 0]
    Solution().sortColors(l)
    print(l)
    l = [2, 0]
    Solution().sortColors(l)
    print(l)
    l = [2]
    Solution().sortColors(l)
    print(l)
    l = [0, 0]
    Solution().sortColors(l)
    print(l)
    l = [2, 2]
    Solution().sortColors(l)
    print(l)
    l = [2, 1]
    Solution().sortColors(l)
    print(l)

