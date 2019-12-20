"""
32、最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解：括号配对问题：栈
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        :param s:
        :return:
        栈+排序    索引索引索引
        利用栈stack存放左括号索引，进行配对
        配对成功索引的放入res列表中， 对列表进行排序后寻找最长的连续
        时间复杂度：O(nlog(n))，括号匹配O(n)，排序复杂度O(nlog(n))，
        寻找最长连续子序列O(n)，总体O(nlog(n))
        空间复杂度：O(n)
        """
        stack = []
        res = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                res.append(stack.pop())
                res.append(i)
        res.sort()
        max_len, i = 0, 0
        while i< (len(res)-1):
            tmp = i
            while i< (len(res)-1) and (res[i+1]-res[i])==1:
                i += 1
            max_len = max(max_len, i-tmp+1)
            i += 1
        return max_len

    def longestValidParentheses2(self, s: str) -> int:
        """
        :param s:
        :return:
        栈 优化
        利用栈stack存放左括号索引，进行配对
        初试化栈stack=[−1]，和结果res=0。栈中元素表示上一不匹配位置索引。
        配对成功索引的放入res列表中， 对列表进行排序后寻找最长的连续
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not s:
            return 0
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                # 若栈为空，表示之前的所有的(匹配成功，上一步出栈的是栈底的−1
                # 或者是前一个不匹配的)。则更新栈底为当前)的索引，表示不匹配的位置。
                if not stack:
                    stack.append(i)
                #
                else:
                    res = max(res, i-stack[-1])
        return res

    def longestValidParentheses3(self, s: str) -> int:
        """
        :param s:
        :return:
        动态规划
        时间复杂度：O(n)
        空间复杂度：O(1)
        dp[i]表示到i位置的最长有效括号的长度。
        """
        if (not s):
            return 0
        res = 0
        n = len(s)
        dp = [0] * n
        for i in range(1, len(s)):
            if (s[i] == ")"):
                if (s[i - 1] == "("):
                    dp[i] = dp[i - 2] + 2
                if (s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "("):
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                res = max(res, dp[i])
        return res



