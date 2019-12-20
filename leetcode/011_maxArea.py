"""
11、盛最多水的容器
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
图例见链接

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解：双指针
    i，j两指针分别指向数组左右
    水量由两支指针的高度的短板决定，
    移动短板去寻找面积更大的区域
    直到，i,j相遇
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height)-1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i]*(j-i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

    def maxArea2(self, height: List[int]) -> int:
        i, j, res = 0, len(height)-1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i]*(j-i))
                temp = height[i]
                while height[i] <= temp and i < j:
                    i += 1
            else:
                res = max(res, height[j] * (j - i))
                temp = height[j]
                while height[j] <= temp and i < j:
                    j -= 1
        return res


