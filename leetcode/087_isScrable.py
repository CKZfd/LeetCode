"""
87、扰乱字符串
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
下图是字符串 s1 = "great" 的一种可能的表示形式。
https://leetcode-cn.com/problems/scramble-string/
"""
"""
分区间
    给定两个字符串T和S，假设T是由S变换而来
    如果T和S长度不一样，必定不能变来
    如果长度一样，顶层字符串S能够划分为S1和S2，同样字符串T也能够划分为T1和T2
        情况一：没交换，S1 ==> T1，S2 ==> T2
        情况二：交换了，S1 ==> T2，S2 ==> T1
"""
import sys
sys.setrecursionlimit(100000) #例如这里设置为十万

class Solution:
    def isScramble(self, s1, s2) :
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    s1 = "great"
    s2 = "rgeat"
    print(s.isScramble(s1, s2))