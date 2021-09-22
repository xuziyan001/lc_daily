"""
发音类似 "try"）或者说 前缀树 是一种树形数据结构，
用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；
否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；
否则，返回 false 。

"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.prefix = [None] * 26
        self.is_end = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for s in word:
            index = ord(s) - ord('a')
            if node.prefix[index] is None:
                node.prefix[index] = Trie()
            node = node.prefix[index]
        node.is_end = True

    def searchPrefix(self, prefix):
        node = self
        for s in prefix:
            index = ord(s) - ord('a')
            if node.prefix[index]:
                node = node.prefix[index]
            else:
                return None
        return node


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        n = self.searchPrefix(word)
        return n is not None and n.is_end == True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.searchPrefix(prefix) is not None
