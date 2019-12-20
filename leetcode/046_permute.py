"""
46、全排列
给定一个没有重复数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解 ： (树 递归) 回溯
注意字符串和列表 可使用 + 法操作，c1+c2 表示将c2接在c1后面
字典不可以使用加法
回溯法
是一种通过探索所有可能的候选解来找出所有的解的算法。
如果候选解被确认 不是 一个解的话（或者至少不是 最后一个 解），
回溯算法会通过在上一步进行一些变化抛弃该解，即 回溯 并且再次尝试。
逐个将nums里的数放进tmp中

"""
class Solution:
    def permute(self, nums) :
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([3, 2, 1]))
