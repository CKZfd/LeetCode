"""
208、实现Trie前缀树
Trie树基本性质. https://zhuanlan.zhihu.com/p/57342852
    根节点为空、每一个节点为一个字母，
    一个节点的子节点字符一定不相同
    从根到某一个节点，拼接长字符串
    Trie提高效率,用空间换时间

"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {} # 表征树

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.root
        for char in word:
            if char not in tree:
                tree[char] = {}
            tree = tree[char]
        # 单词结束标志
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.root
        for char in word:
            if char not in tree:
                return False
            tree = tree[char]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.root
        for char in prefix:
            if char not in tree:
                return False
            tree = tree[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)