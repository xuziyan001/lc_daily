"""
所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。
在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

"""
from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        res = []
        d = defaultdict(lambda :0)
        for i in range(10, len(s)+1):
            d[s[i-10:i]] += 1
        for k, v in d.items():
            if v >= 2:
                res.append(k)
        return res


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(s))
    s = "AAAAAAAAAAAAA"
    print(Solution().findRepeatedDnaSequences(s))
