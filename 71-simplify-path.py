class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        name = ''
        path += '/'
        for each in path:
            if each == '/':
                if name == '.':
                    pass
                elif name == '..':
                    if len(stack) == 0:
                        pass
                    else:
                        stack.pop()
                elif name != '':
                    stack.append(name)
                else:
                    pass
                name = ''
            else:
                name += each
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    path = '/home//dd/sd../s/e3./1/2/3/../3/3/3/..'
    print(Solution().simplifyPath(path))
    path = '/../'
    print(Solution().simplifyPath(path))
