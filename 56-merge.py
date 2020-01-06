from typing import List


class Solution:

    def __init__(self):
        self.m = []

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for interval in intervals:
            interval.sort()
            imin = interval[0]
            imax = interval[1]
            mmin, mmax = imin, imax
            for each in self.m:
                if each[0] <= imin <= each[1]:
                    mmin = each[0]
                if each[0] <= mmax <= each[1]:
                    mmax = each[1]
            to_remove = []
            for each in self.m:
                if each[0] >= mmin and each[1] <= mmax:
                    to_remove.append(each)
            for each in to_remove:
                self.m.remove(each)
            self.m.append([mmin, mmax])
        return self.m


if __name__ == '__main__':
    print(Solution().merge([[1,2], [3,4]]))
    l = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution().merge(l))


