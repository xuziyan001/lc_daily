from typing import List


class Solution:

    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        for num in nums:
            t = nums.copy()
            t.remove(num)
            self.bfs([num], t)
        return self.res

    def bfs(self, current: List[int], remain: List[int]):
        if not remain:
            self.res.append(current)
        for each in remain:
            t = current.copy()
            t.append(each)
            tt = remain.copy()
            tt.remove(each)
            self.bfs(t, tt)


if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().permute(nums))
