class Node:
    def __init__(self, n):
        self.v = n
        self.left = None
        self.right = None


def construct_tree(l):
    if len(l) == 0:
        return None
    root = Node(l[0])
    for value in l[1:]:
        n = Node(value)
        start = root
        while start:
            if value > start.v and start.right == None:
                start.right = n
                break
            elif value > start.v and start.right != None:
                start = start.right
            elif value <= start.v and start.left == None:
                start.left = n
                break
            else:
                start = start.left
    return root


def p(root):
    if root is None:
        return
    print(root.v)
    p(root.left)
    p(root.right)


if __name__ == '__main__':
    l = list(range(10))
    p(construct_tree(l))
