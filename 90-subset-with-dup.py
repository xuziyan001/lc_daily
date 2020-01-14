from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrace(index=0, current=[]):
            if tuple(current) not in s:
                res.append(current[:])
                s.add(tuple(current))
            for i in range(index, n):
                current.append(nums[i])
                backtrace(i+1, current)
                current.pop()
        res = []
        s = set()
        nums.sort()
        n = len(nums)
        backtrace()
        return res


if __name__ == '__main__':
    l = [1,2,2,2]
    print(Solution().subsetsWithDup(l))
    l = [1,2]
    print(Solution().subsetsWithDup(l))
