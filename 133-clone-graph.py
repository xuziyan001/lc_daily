"""
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表
"""
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        stack = deque()
        stack.append(node)
        visited = set()
        new_created = dict()
        while stack:
            current = stack.popleft()
            if current.val not in visited:
                if current.val in new_created:
                    new_node = new_created[current.val]
                else:
                    new_node = Node(current.val)
                    new_created[current.val] = new_node
                visited.add(current.val)
                new_neighbors = []
                for nei in current.neighbors:
                    stack.append(nei)
                    if nei.val in new_created:
                        new_neighbors.append(new_created[nei.val])
                    else:
                        tmp = Node(nei.val)
                        new_created[nei.val] = tmp
                        new_neighbors.append(tmp)
                new_node.neighbors = new_neighbors
        return new_created[1]


if __name__ == '__main__':
    n1,n2,n3,n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = []
    print(Solution().cloneGraph(None))