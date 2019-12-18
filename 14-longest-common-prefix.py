from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        strs.sort()
        common = strs[0]
        for i in range(len(common), -1, -1):
            tmp = common[:i]
            matched = True
            for each in strs[1:]:
                if each[:i] != tmp:
                    matched = False
                    break
            if matched:
                return tmp


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["abca","abc"]))
