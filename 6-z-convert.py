class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = []
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                j = 0
                nx = i + (numRows-1) * 2 * j
                while nx < len(s):
                    res.append(s[nx])
                    j += 1
                    nx = i + (numRows - 1) * 2 * j
            else:
                j = 0
                nx1 = i + (numRows-1) * 2 * j
                nx2 = nx1 + (numRows-i-1) * 2
                while nx1 < len(s):
                    res.append(s[nx1])
                    if nx2 < len(s):
                        res.append(s[nx2])
                    j += 1
                    nx1 = i + (numRows - 1) * 2 * j
                    nx2 = nx1 + (numRows-i-1) * 2
        return ''.join(res)


if __name__ == '__main__':
    r = Solution().convert("LEETCODEISHIRING", 3)
    print(r)
    print(r == "LCIRETOESIIGEDHN")
    r = Solution().convert("LEETCODEISHIRING", 4)
    print(r)
    print(r == "LDREOEIIECIHNTSG")
    r = Solution().convert("L", 1)
    print(r)
    print(r == "L")
    r = Solution().convert("", 4)
    print(r)
    print(r == "")
