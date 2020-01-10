from typing import List


"""
这里压栈思维层级比较高
"""

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        res = 0
        if len(heights) == 0:
            return 0
        for i in range(0, len(heights)):
            if len(stack) == 1:
                stack.append(i)
                continue
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                    t = stack.pop()
                    max_area = heights[t] * (i-1-stack[-1])
                    res = max(res, max_area)
                stack.append(i)
        while stack[-1] != -1:
            i = len(heights)
            t = stack.pop()
            max_area = heights[t] * (i-1-stack[-1])
            res = max(res, max_area)
        return res

    def largestRectangleArea2(self, heights: List[int]) -> int:
        m = 0
        n = len(heights)
        for i in range(n):
            for j in range(i, n):
                area = (j-i+1) * min(heights[i:j+1])
                if area > m:
                    m = area
        return m


if __name__ == '__main__':
    l = [2,1,5,6,2,3] #10
    print(Solution().largestRectangleArea(l))
    l = [4,5,6,4,5,6]
    print(Solution().largestRectangleArea(l))
    l = [6, 4, 5, 2, 4, 3, 9] #14
    print(Solution().largestRectangleArea(l))
    l = list(range(1,20000))
    print(Solution().largestRectangleArea(l))
