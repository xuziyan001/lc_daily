


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
            if r.next:
                r.right.next = r.next.left
            connnectTwo(r.left)
            connnectTwo(r.right)
        connnectTwo(root)
        return root


