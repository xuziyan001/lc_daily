from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        h = [[] for i in range(1000)]
        max_num = nums[0]
        for each in nums:
            if each <= 0:
                continue
            if each > max_num:
                max_num = each
            mod = each % 1000
            h[mod].append(each)
        for i in range(1, max_num):
            mod = i % 1000
            if i in h[mod]:
                continue
            else:
                return i
        if max_num <= 0:
            return 1
        return max_num + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([0,1,2]))
    print(Solution().firstMissingPositive([3,4,-1,1]))
    print(Solution().firstMissingPositive([7,8,9,11,12]))
