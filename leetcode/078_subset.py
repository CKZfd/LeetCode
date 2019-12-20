"""
78、子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
子集问题、组合问题：
    问题分解：将问题的规模缩小。考虑数目为n-1的情况
    [1,2,3] 的子集 = [1, 2]的子集 + [1,2]的各个子集与[3]组和的子集
    自底向上
迭代法：
    []的子集为 res=[[]]
    迭代增加问题的规模 for num in nums:
        res = res + [ [num] + re for re in res] 
        ([1]_res = [[]] + [ [1] + [] ])
        ([2]_res = [ [],[1] ] + [ [2] + [], [2] + [1] ])

回溯法: 一种自底向上的递归方法？
    res = [] 
    track_back(0,[]) 从0，以空集开始
    n = len(nums)  重复使用
    def track_back(start, tmp):
        res.append(tmp)
        for i in range(start, n):
            track_back(i+1, nums[i] + tmp)
    
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res = res + [[n] + num for num in res]
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res



if __name__ == "__main__":
    # s = Solution()
    s1 = [1, 2, 3, 4, 6]
    t1 = [1, 2, 3, 4, 5]
    print (s1+t1)
    # print(s.minWindow(s1,t1))