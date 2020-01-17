from tool import TreeNode, concat_tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
                return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    l = [3,1,4,None,None,2]
    print(Solution().isSameTree(concat_tree(l), concat_tree(l)))
    l2 = l[:]
    l2[-1], l2[-2] = l2[-2], l2[-1]
    print(concat_tree(l2))
    print(Solution().isSameTree(concat_tree(l), concat_tree(l2)))

