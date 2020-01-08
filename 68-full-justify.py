from functools import reduce
from operator import add
from typing import List


"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = ''
        for word in words:
            if len(line) + len(word) == maxWidth:
                line += word
                res.append(line)
                line = ''
            elif len(line) + len(word) < maxWidth:
                line += word + ' '
            else:
                l = self.justify(line, maxWidth)
                res.append(l)
                line = word + ' '
        line = line.strip()
        if line:
            res.append(line + ' ' * (maxWidth-len(line)))
        return res

    def justify(self, line: str, maxWidth: int) -> str:
        l = line.strip().split(' ')
        n = len(l)
        count = reduce(add, [len(x) for x in l], 0)
        if n == 1:
            return l[0] + (maxWidth-count) * ' '
        remain = maxWidth - count
        i, j = divmod(remain, n-1)
        for t in range(j):
            l.insert(2*t+1, ' '*(i+1))
        for t in range(j, n-1):
            l.insert(2*t+1, ' '*i)
        return ''.join(l)


if __name__ == '__main__':
    #words = ["This", "is", "an", "example", "of", "text", "justification."]
    #words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    #maxWidth = 16
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    l = Solution().fullJustify(words, maxWidth)
    for each in l:
        print(each)
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 14
    l = Solution().fullJustify(words, maxWidth)
    for each in l:
        print(each)
        print(len(each))
