"""
5、最长回文字符串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解：
中心扩散法：遍历每一个索引，以这个索引为中心，
        利用“回文串”中心对称的特点，往两边扩散，看最多能扩散多远。
    枚举“中心位置”时间复杂度为 O(N)，从“中心位置”扩散得到“回文子串”的时间复杂度为 O(N)，
    因此时间复杂度可以降到O(N^2)。
    注意：回文串在长度为奇数和偶数的时候，“回文中心”的形式是不一样的。
    我们可以设计一个方法，兼容以上两种情况：
    1、如果传入重合的索引编码，进行中心扩散，此时得到的回文子串的长度是奇数；
    2、如果传入相邻的索引编码，进行中心扩散，此时得到的回文子串的长度是偶数。


"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2: return s
        max_len = 1
        res = s[0]

        for i in range(length-1):
            # 奇偶两种情况
            palindrome_odd, odd_len = self.__center_spread(s, length, i, i)
            palindrome_even, even_len = self.__center_spread(s, length, i, i+1)
            if odd_len >= even_len:
                cur_maxsub, cur_maxlen = palindrome_odd, odd_len
            else:
                cur_maxsub, cur_maxlen = palindrome_even, even_len
            if cur_maxlen > max_len:
                max_len = cur_maxlen
                res = cur_maxsub
        return res


    def __center_spread(self, s, length, left, right):
        """
            left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
            right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        i, j = left, right
        while i >=0 and j<length and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j], j-i-1


if __name__ == '__main__':
    # begin
    s = Solution()
    s1 = "babad"
    print(s.longestPalindrome(s1))
