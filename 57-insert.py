from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = -1, -1
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                left = i
            if intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                right = i
        mmin, mmax = newInterval[0], newInterval[1]
        if left != -1:
            mmin = intervals[left][0]
        if right != -1:
            mmax = intervals[right][1]
        intervals = list(filter(lambda x: x[1] < mmin or x[0] > mmax, intervals))
        s = 0
        for each in intervals:
            if each[0] > mmin:
                break
            s += 1
        intervals.insert(s, [mmin, mmax])
        return intervals


if __name__ == '__main__':
    l = [[1,3],[6,9]]
    r = [2,5]
    print(Solution().insert(l,r))
    l = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    r = [4,8]
    print(Solution().insert(l, r))
