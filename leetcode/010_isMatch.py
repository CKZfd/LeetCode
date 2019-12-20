"""
10、正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
说明:
	s 可能为空，且只包含从 a-z 的小写字母。
	p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。
    因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。
    因此可以匹配字符串 "aab"。
示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
题解
字符+∗是一个整体，表示这个字符出现0次或者多次！ * 不单独出现
在P中每一个非*（？）字符都要判断后一位是否接的是*
特别.* 表示可匹配零个或多个任意字符
设计一个状态 dp(i,j) 表征 

动态规划法
重叠子问题结构
0、初始化s的长度S，p的长度P
1、初始化哈希表memo={}，键为(i,j)，值为True or False，
表示s[0,...,i]和p[0,...,j]是否匹配。
2、定义递归函数dp(i,j)，i为当前s的匹配位置，j为p的匹配位置。
若(i,j)出现在memo中，表示当前子问题，之前已经处理过，直接返回对应的值，memo[(i,j)]
若j==P，说明p已经匹配完，若此时s还有字符未匹配，则返回False，若s也匹配完，则返回True。即返回i==S
定义pre表示当前p和s的首位是否匹配。
    条件：i<S表示s是否遍历完。且p[j]是否等于s[i]或"."。pre=i<S and p[j] in {s[i],"."}pre= i<S\ and\ p[j]\ in\ \{s[i],"."\}pre=i<S and p[j] in {s[i],"."}。
判断是否存在∗字符，
    条件：j<=P−2表示是否还剩两个字符以上，且p[j+1]为∗：
        跳过这两个字符，表示匹配0次，dp(i,j+2)
        首位匹配成功，继续匹配下一位，pre and dp(i+1,j)
        tmp=dp(i,j+2) or pre and dp(i+1,j)
否则，tmp=dp(i+1,j+1)
更新memo，memo[(i,j)]=tmp
返回tmp
返回dp(0,0)

"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S = len(s)
        P = len(p)
        memo = {}
        def dp(i, j):
            if ((i, j) in memo):
                return memo[(i, j)]
            if (j == P):
                return i == S
            pre = i < S and p[j] in {s[i], "."}
            if (j <= P - 2 and p[j + 1] == "*"):
                tmp = dp(i, j + 2) or pre and dp(i + 1, j)
            else:
                tmp = pre and dp(i + 1, j + 1)
            memo[(i, j)] = tmp
            return tmp
        return dp(0, 0)


    def isMatch2(self, s: str, p: str) -> bool:
        S, P = len(s), len(p)
        def dp(i, j):
            if j == P: return i == S
            pre = i < S and p[j] in {s[i], "."}
            if j <= P - 2 and p[j + 1] == "*":
                tmp = dp(i, j + 2) or pre and dp(i + 1, j)
            else:
                tmp = dp(i + 1, j + 1)
            return tmp
        return dp(0, 0)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isMatch("ab", ".*c"))

















