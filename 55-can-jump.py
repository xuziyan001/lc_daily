from typing import List


class Solution:
    def canJumpDfs(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        num = nums[0]
        if num >= len(nums)-1:
            return True
        if num == 0:
            return False
        for i in range(num, 0, -1):
        #for i in range(1, num+1, 1):
            next = nums.copy()[i:]
            if self.canJump(next):
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        num = nums[0]
        if num >= len(nums)-1:
            return True
        if num == 0:
            return False
        range_min = 1
        range_max = num
        while range_max < len(nums)-1:
            t_min, t_max = range_min, range_max
            for i in range(range_min, range_max+1):
                m = i + nums[i]
                if m > t_max:
                    t_max = m
                    t_min = i
            if t_max == range_max:
                return False
            range_min, range_max = t_min, t_max
        return True


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))
    nums = [1,1,1,0]
    print(Solution().canJump(nums))
    nums = [2,5,0,0]
    print(Solution().canJump(nums))
    nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print(Solution().canJump(nums))
    nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    print(Solution().canJump(nums))
