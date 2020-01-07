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
            self.m = list(filter(lambda x: x[0] < mmin or x[1] > mmax, self.m))
            self.m.append([mmin, mmax])
        return self.m


if __name__ == '__main__':
    print(Solution().merge([[1,2], [3,4]]))
    l = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution().merge(l))


