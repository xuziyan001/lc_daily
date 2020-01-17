from typing import List
from tool import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def iter(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                left = iter(start, i-1)
                right = iter(i+1, end)
                for l in left:
                    for r in right:
                        current = TreeNode(i)
                        current.left = l
                        current.right = r
                        res.append(current)
            return res
        if n == 0:
            return []
        return iter(1, n)


if __name__ == '__main__':
    print(Solution().generateTrees(3))
    print(Solution().generateTrees(0))
