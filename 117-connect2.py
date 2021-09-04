

class Solution:
    def connect(self, root):
        if not root:
            return root
        # root.next = None
        start = root
        while start:
            self.nextStart = None
            self.last = None
            def connnectTwo(r):
                if r is None:
                    return
                if self.nextStart is None:
                    self.nextStart = r
                if self.last:
                    self.last.next = r
                self.last = r
            p = start
            while p:
                connnectTwo(p.left)
                connnectTwo(p.right)
                p = p.next
            start = self.nextStart
        return root
