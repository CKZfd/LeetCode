"""
3、无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解：滑动窗口法 双指针定左右
    每当在有一个元素出现，判断窗口里是否已经有这个数据，
    如果有，需要向右移动窗口（左指针向右移动，直到，窗口中不含有该元素时将其加入）
    需要记录窗口的当前长度， 以及历史的最大长度，直到右指针遍历到字符串尾
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        look_up = set()
        left = 0
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in look_up:
                look_up.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            look_up.add(s[i])
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not s: return 0
        left = 0
        max_len = 0
        cur_len = 0
        for right in range(len(s)):
            while s[right] in s[left:right]:
                left += 1
                cur_len -= 1
            cur_len += 1
            if cur_len > max_len: max_len = cur_len
        return max_len


if __name__ == '__main__':
    # begin
    s = Solution()
    s1 = "012534567589"
    print(s.lengthOfLongestSubstring2(s1))
    print(s1[0:9])