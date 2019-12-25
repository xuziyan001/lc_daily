from typing import List


class Solution:

    def __init__(self):
        self.result = []
        self.candidates = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.backtrace([], target, 0)
        return self.result

    def backtrace(self, path, target, start):
        if target < 0:
            return
        if target == 0:
            self.result.append(path)
            return
        else:
            for i in range(start, len(self.candidates)):
                path.append(self.candidates[i])
                self.backtrace(path.copy(), target-self.candidates[i], i)
                path.pop()


if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7], 7))
    print(Solution().combinationSum([2,3,5], 8))
