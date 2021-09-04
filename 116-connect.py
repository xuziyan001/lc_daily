"""
给定一个完全二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

"""


class Solution:
    def connect(self, root):
        if not root:
            return root
        # root.next = None
        if not root.left:
            return root
        # root.left.next = root.right
        def connnectTwo(r):
            if not r.left:
                return
            r.left.next = r.right
            # 这一步很关键，利用root.next找到两颗不同子树的链接
            if r.next:
                r.right.next = r.next.left
            connnectTwo(r.left)
            connnectTwo(r.right)
        connnectTwo(root)
        return root


