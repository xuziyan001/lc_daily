from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        current = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= current:
                current = nums[i]
                continue
            else:
                # 降序的第一个值
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                # reverse [i+1:]
                for j in range((len(nums)-i-1) // 2):
                    nums[i+1+j], nums[len(nums)-1-j] = nums[len(nums)-1-j], nums[i+1+j]
                return
        # 全升序，翻转
        for j in range(len(nums) // 2):
            nums[j], nums[len(nums) - 1 - j] = nums[len(nums) - 1 - j], nums[j]


if __name__ == '__main__':
    l = [1,2,3,4]
    print(Solution().nextPermutation(l))
    print(l)
    l = [1,2,3,5,2,3,4,1]
    print(Solution().nextPermutation(l))
    print(l)
    l = [2,3,1]
    print(Solution().nextPermutation(l))
    print(l)
    l = [1, 3, 2]
    print(Solution().nextPermutation(l))
    print(l)
    l = [5,1,1]
    print(Solution().nextPermutation(l))
    print(l)
