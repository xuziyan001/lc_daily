"""
现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。
给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，
表示在选修课程 ai 前 必须 先选修 bi 。

例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，
你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。

"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses < 2:
            return list(range(numCourses))
        edges = defaultdict(list)
        indre = defaultdict(lambda: 0)
        for pre in prerequisites:
            edges[pre[1]].append(pre[0])
            indre[pre[0]] += 1
        res = []
        queue = deque([x for x in range(numCourses) if indre[x] == 0])
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for each in edges[cur]:
                indre[each] -= 1
                if indre[each] == 0:
                    queue.append(each)
        if len(res) != numCourses:
            return []
        return res


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(Solution().findOrder(4, prerequisites))
