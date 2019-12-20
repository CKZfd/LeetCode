"""
84、柱状图中的最大矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""
"""
题解：分治法
通过观察，可以发现，最大面积矩形存在于以下几种情况：
    确定了最矮柱子以后，矩形的宽尽可能往两边延伸。
    在最矮柱子左边的最大面积矩形（子问题）。
    在最矮柱子右边的最大面积矩形（子问题）。
最坏情况：有序
优化：可以用线段树代替遍历来找到区间最小值。
中心扩展
单调栈
维护一个单调递增的栈，
从中心扩展法可以发现，以height[i]构建矩形，
其左右边界在坐标系中会显示为一个倒V型，；
如果左右边界能向外扩展的话，那么会由中心向左单调递增，中心向右也呈现单调递增性，类V型。
对于这种出现单调性的题目，通常可以考虑使用单调栈进行求解。
考虑维护一个单调递增栈stack，stack中存储对应的索引值，
如果h[i] < h[stack.top]，那么对于stack.top来说即遇到了右边界，
此时由于stack的单调递增性，
那么在stack.top底部的下一个索引即对应着stack.top的左边界。

向右找到一个不再递增的高度h，，依次向左逐个把高于h的出栈
(i-1 -stack[-1])*heights[tmp]
其中i-1指向h前一个元素，stack[-1]栈顶
heights[tmp]为 stack[-1]（不含）到 i（不含） 的最低高度
出栈1个 s = 1 * 当前高度


"""
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        heights = [0] + heights + [0] # 确保左右边界最小，呈倒V型
        res = 0
        for i in range(len(heights)):
            # 当栈不为空，且当前值入栈无法维持单调递增的栈时
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                # 面积的计算：将大于heights[i]的逐个出栈，作为高，
                # 宽为栈顶与i (均不含) 的宽度
                res = max(res, (i-1 -stack[-1])*heights[tmp])
            # 新元素入栈，栈继续为单调
            stack.append(i)
        return res

    # 分治法
    def largestRectangleArea2(self, heights) :
        n = len(heights)
        def max_area(heights):
            length = len(heights)
            if length == 0:
                return 0
            min_i = 0
            for i in range(length):
                if heights[i] < heights[min_i]:
                    min_i = i
            s = heights[min_i]*length
            return max(max_area(heights[:min_i]), s, max_area(heights[min_i+1:]))

        return max_area(heights)

if __name__ == '__main__':
    # begin
    s = Solution()
    s1 = [2,1,5,6,2,3]
    print(s.largestRectangleArea2(s1))

