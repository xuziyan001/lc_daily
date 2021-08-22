#
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
#输入：nums = [-10,-3,0,5,9]
#输出：[0,-3,9,-10,null,5]
#解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree



from typing import List

from tool import TreeNode, concat_tree


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[n//2])
        root.left = self.sortedArrayToBST(nums[:n//2])
        root.right = self.sortedArrayToBST(nums[n//2+1:])
        return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    r = Solution().sortedArrayToBST(nums)
    print(r)



