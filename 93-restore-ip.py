"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        l = len(s)
        if l > 32 or l < 4:
            return []

        def restore(remains=s, current=[]):
            if len(remains) == 0:
                if len(current) == 4:
                    res.append('.'.join(current))
                return
            current.append(remains[0])
            restore(remains[1:], current)
            current.pop()
            if len(remains) >= 2 and remains[0] != '0':
                current.append(remains[:2])
                restore(remains[2:], current)
                current.pop()
            if len(remains) >= 3 and remains[0] != '0' and int(remains[:3]) <= 255:
                current.append(remains[:3])
                restore(remains[3:], current)
                current.pop()
        res = []
        restore()
        return res


if __name__ == '__main__':
    l = "25525511135"
    print(Solution().restoreIpAddresses(l))
    l = "0000"
    print(Solution().restoreIpAddresses(l))
