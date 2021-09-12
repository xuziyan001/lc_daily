"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""
from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 第一步：定义比较函数，把最大的放左边
        # 第二步：排序
        # 第三步：返回结果
        def compare(x, y): return int(y+x) - int(x+y)
        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        return "0" if nums[0]=="0" else "".join(nums)


if __name__ == '__main__':
    l = [3,30,34,5,9]
    s = Solution().largestNumber(l)
    print(s)