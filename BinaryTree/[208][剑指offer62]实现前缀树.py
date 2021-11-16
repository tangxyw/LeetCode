from typing import Union


class TrieNode:
    """前缀树的节点类"""

    def __init__(self):
        # 子节点用dict表示, key为字母a-z, value为TrieNode
        self.children = {}
        # 是否为单词节点标志
        self.is_word = False


class Trie:
    # https://www.cnblogs.com/luosongchao/p/3239521.html

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """在前缀树中插入单词word"""
        node = self.root
        # 遍历单词中每一个字母
        for c in word:
            if c not in node.children:  # 上一级节点的子节点中没有当前字母, 新增
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True  # 遍历结束后, 在最后一个字母对应的节点上打上标记

    def _search_prefix(self, word: str) -> Union[TrieNode, None]:
        """内部方法, 判断输入word是否是一个前缀"""
        node = self.root
        for c in word:
            if c not in node.children:  # 不是前缀, 返回None
                return None
            node = node.children[c]
        return node  # 是前缀, 返回最后一个字母对应的节点

    def search(self, word: str) -> bool:
        """在前缀树中查询单词word"""
        node = self._search_prefix(word)
        # 当word在前缀树中, 且最后一个字母对应的标志为真时, 返回True
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """在前缀树中寻找路径prefix"""
        return self._search_prefix(prefix) is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
