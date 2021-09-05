"""
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

"""
from tool import TreeNode, concat_tree

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.__dfs(root, ['0'])

    def __dfs(self, r, current):
        if not r.left and not r.right:
            current.append(str(r.val))
            return int(''.join(current))
        current.append(str(r.val))
        left, right = 0, 0
        if r.left:
            left = self.__dfs(r.left, current[:])
        if r.right:
            right = self.__dfs(r.right, current[:])
        return left + right


if __name__ == '__main__':
    l = [4,9,0,5,1]
    print(Solution().sumNumbers(concat_tree(l)))
    l = [4,9,0,None,1]
    print(Solution().sumNumbers(concat_tree(l)))
