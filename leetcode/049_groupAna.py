"""
49、字母异味词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
	所有输入均为小写字母。
	不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
当且仅当它们的排序字符串相等时，两个字符串是字母异位词。
其中每个键 
K 是一个排序字符串，每个值是初始输入的字符串列表，排序后等于 K。
"""

class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        # defaultdict是Python内建dict类的一个子类，第一个参数为default_factory属性提供初始值，
        # 默认为None。它覆盖一个方法并添加一个可写实例变量。它的其他功能与dict相同，
        # 但会为一个不存在的键提供默认值，从而避免KeyError异常。
        lookup = defaultdict(list) # 参数为字典的value的类型
        for s in strs:
            lookup["".join(sorted(s))].append(s)
        return list(lookup.values())

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
