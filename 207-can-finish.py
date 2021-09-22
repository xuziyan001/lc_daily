import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = collections.defaultdict(lambda: 0)

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        queue = collections.deque([x for x in range(numCourses) if x not in indeg])
        count = 0
        while queue:
            count += 1
            current = queue.popleft()
            for each in edges[current]:
                indeg[each] -= 1
                if indeg[each] == 0:
                    queue.append(each)
        return count == numCourses

