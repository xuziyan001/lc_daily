from typing import List


class Solution:

    def __init__(self):
        self.result = []
        self.candidates = []
        self.dup = set()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.backtrace([], target, 0)
        return self.result

    def backtrace(self, path, target, start):
        if target < 0:
            return
        if target == 0:
            if tuple(path) in self.dup:
                return
            else:
                self.dup.add(tuple(path))
                self.result.append(path)
            return
        else:
            for i in range(start, len(self.candidates)):
                path.append(self.candidates[i])
                self.backtrace(path.copy(), target-self.candidates[i], i+1)
                path.pop()


if __name__ == '__main__':
    print(Solution().combinationSum([10,1,2,7,6,1,5], 8))
