"""
56、合并区间
给出一个区间的集合，请合并所有重叠的区间。
示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
！！！集合：不一定有序 
遍历：比较上一个的右区间 和 这一个的 左区间（右？？？）
    可以合并：左区间替换，并移除前一个 
"""

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals)
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i][0] = intervals[i-1][0]
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
                intervals.pop(i-1)
                i -= 1
            i += 1
        return intervals
if __name__ == "__main__":
    s = Solution()
    inter = [[2,3],[1,6],[8,10],[5,18]]
    print(s.merge(inter))