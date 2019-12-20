"""
76、最小覆盖字串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：
    如果 S 中不存这样的子串，则返回空字符串 ""。
    如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
滑动窗口,左右指针定窗口
滑动窗口算法的思路是这样：
1、我们在字符串 S 中使用双指针中的左右指针技巧，
    初始化 left = right = 0，把索引闭区间 [left, right] 称为一个「窗口」。
2、我们先不断地增加 right 指针扩大窗口 [left, right]，
    直到窗口中的字符串符合要求（包含了 T 中的所有字符）。
3、此时，我们停止增加 right，转而不断增加 left 指针缩小窗口 [left, right]，
    直到窗口中的字符串不再符合要求（不包含 T 中的所有字符了）。
    同时，每次增加 left，我们都要更新一轮结果。
4、重复第 2 和第 3 步，直到 right 到达字符串 S 的尽头。
这个思路其实也不难，第 2 步相当于在寻找一个「可行解」，然后第 3 步在优化这个「可行解」，最终找到最优解。左右指针轮流前进，窗口大小增增减减，窗口不断向右滑动。

如何确定窗口中的字符串包含了T中的所有字符串：
用一个哈希表 needs 记录字符串 t 中包含的字符及出现次数，
用另一个哈希表 window 记录当前「窗口」中包含的字符及出现的次数，
如果 window 包含所有 needs 中的键，且这些键对应的值都大于等于 needs 中的值，
那么就可以知道当前「窗口」符合要求了

作者：labuladong
链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/hua-dong-chuang-kou-suan-fa-tong-yong-si-xiang-by-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

作者：labuladong
链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/hua-dong-chuang-kou-suan-fa-tong-yong-si-xiang-by-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def minWindow(self, s, t) :
        if not s or not t:
            return ""
        left = right = 0
        needs, window = {}, {}
        min_len = 10000
        min_sub = [0,0]
        for char in t:
            if char in needs:
                needs[char] += 1
            else:
                needs[char] = 1

        def t_in_sWin(needs, window):
            for key in needs.keys():
                if key not in window:
                    return False
                elif needs[key] > window[key]:
                    return False
            return True

        while right < len(s):
            while not t_in_sWin(needs, window) and right < len(s):
                if s[right] in window:
                    window[s[right]] += 1
                else:
                    window[s[right]] = 1
                right += 1
            # 边界条件  到达边界，且没有找到的情况
            if not t_in_sWin(needs, window) and right == len(s):
                break

            while t_in_sWin(needs, window):
                if window[s[left]] > 1:
                    window[s[left]] -= 1
                else:
                    del window[s[left]]
                left += 1
            if right-left+1 < min_len:
                min_len = right-left+1
                min_sub = [left-1, right]
        # if min_sub[0] == min_sub[1]:
        #     return ""
        return s[min_sub[0]:min_sub[1]]

if __name__ == "__main__":
    s = Solution()
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(s.minWindow(s1,t1))

