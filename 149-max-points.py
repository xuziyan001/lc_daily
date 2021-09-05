"""
给你一个数组 points ，
其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ans = 0
        def gcd(x, y):
            while x != 0:
                x, y = y % x, x
            return y
        for i, point in enumerate(points):
            if ans >= n-i or ans > n//2: #?
                break
            cnt = defaultdict(lambda: 0)
            for each in points[i+1:]:
                xx, yy = each[0]-point[0], each[1] - point[1]
                if xx == 0:
                    yy = 1
                elif yy == 0:
                    xx = 1
                else:
                    if yy < 0:
                        xx, yy = -xx, -yy
                    g = gcd(xx, yy)
                    xx /= g
                    yy /= g
                cnt[(xx,yy)] += 1
            for k, v in cnt.items():
                ans = max(ans, v+1)
        return ans
