from tool import TreeNode, concat_tree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = root.left
        right = root.right
        if left:
            if left.val >= root.val:
                return False
        if right:
            if right.val <= root.val:
                return False
        if not (self.isValidBST(left) & self.isValidBST(right)):
            return False
        # 找到左子树最大值与右子树最小值
        left_max = root.val-1
        while left:
            left_max = left.val
            left = left.right
        right_min = root.val+1
        while right:
            right_min = right.val
            right = right.left
        return (root.val > left_max) & (root.val < right_min)


if __name__ == '__main__':
    l = concat_tree([5,1,4,None,None,3,6])
    print(l)
    print(Solution().isValidBST(l))
    l = concat_tree([2,1,3])
    print(Solution().isValidBST(l))
    l = concat_tree([10,5,15,None,None,6,20])
    print(l)
    print(Solution().isValidBST(l))
