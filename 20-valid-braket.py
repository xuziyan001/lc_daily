class Solution:
    def isValid(self, s: str) -> bool:
        left = '([{'
        right = ')]}'
        result = []
        for each in s:
            if each in left:
                result.append(left.index(each))
            elif each in right:
                if len(result) == 0:
                    return False
                if each == right[result.pop()]:
                    continue
                else:
                    return False
            else:
                return False
        return len(result) == 0


if __name__ == '__main__':
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid('([)]'))
