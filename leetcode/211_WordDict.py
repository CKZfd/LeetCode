"""
211. 添加与搜索单词 - 数据结构设计
设计一个支持以下两种操作的数据结构：
void addWord(word)
bool search(word)

search(word) 可以搜索文字或正则表达式字符串，
字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
"""
"""
参考208：字典树、前缀树
    根节点为空、每一个节点为一个字母，
    一个节点的子节点字符一定不相同
    从根到某一个节点，拼接长字符串
    Trie提高效率,用空间换时间
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.root
        for char in word:
            if char not in tree:
                tree[char] = {}
            tree = tree[char]
        # 单词结束标志
        tree['end'] = 'end'


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cut = False

        def f(root, chars):  # 深搜，参数为：当前子字典，当前串
            nonlocal cut
            if cut:  # 剪枝
                return True
            t = root
            for i, c in enumerate(chars):
                if c == '.':
                    return sum(f(t[j], chars[i + 1:]) for j in t if j != 'end')  # 深搜扩展
                if c not in t:
                    return False
                t = t[c]
            cut = 'end' in t
            return cut

        return f(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)