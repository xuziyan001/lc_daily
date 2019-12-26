from typing import List


"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].

"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        mid = sums / 2
        nums.sort(reverse=True)
        return self.find(mid, nums)

    def find(self, target, leftovers):
        if target == 0:
            return True
        if target < 0:
            return False
        previous = -1000
        for each in leftovers:
            if each == previous:
                continue
            l = leftovers.copy()
            l.remove(each)
            previous = each
            res = self.find(target-each, l)
            if res:
                return True
        return False

    def canPartitionPack(self, nums: List[int]) -> bool:
            size = len(nums)

            # 特判，如果整个数组的和都不是偶数，就无法平分
            s = sum(nums)
            if s & 1 == 1:
                return False

            # 二维 dp 问题：背包的容量
            target = s // 2
            dp = [[False for _ in range(target + 1)] for _ in range(size)]

            # 先写第 1 行：看看第 1 个数是不是能够刚好填满容量为 target
            for i in range(target + 1):
                dp[0][i] = False if nums[0] != i else True
            # i 表示物品索引
            for i in range(1, size):
                # j 表示容量
                for j in range(target + 1):
                    if j >= nums[i]:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                    else:
                        dp[i][j] = dp[i - 1][j]

            return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().canPartition([1,5,11,5]))
    print(Solution().canPartition([1,2,3,5]))
    print(Solution().canPartition([1,5,13,5]))
    print(Solution().canPartition([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]))
