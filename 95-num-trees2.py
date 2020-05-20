"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
"""
"""
思路是从列表中选出一个节点作为根，然后左右分割列表作为其左右子树，构成了一个子问题
之所以不交换是需要满足二叉搜索树的条件
"""

from typing import List
from tool import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def iter(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                # i是根节点
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
    print(Solution().generateTrees(6))
