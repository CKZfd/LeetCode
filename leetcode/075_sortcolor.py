"""
75、颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，
原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
注意:
不能使用代码库中的排序函数来解决这道题。
示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：
    一个直观的解决方案是使用计数排序的两趟扫描算法。
    首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
    你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
要求：原地操作
基础方法：快排
上升方法：三指针, 三路快排
定义0的右界bound_0=0，2的左界bound_2=n−1，n为数组长度。cur为当前元素。
因为curr左边的值已经扫描过了，所以curr要++继续扫描下一位，
而与p2交换的值，curr未扫描，要停下来扫描一下，所以curr不用++。
"""


def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    bound_0, bound_2, cur = 0, n-1, 0
    while cur<=bound_2:
        if nums[cur] == 0:
            nums[cur], nums[bound_0] = nums[bound_0], nums[cur]
            bound_0 += 1
            cur += 1
        elif nums[cur] == 2:
            nums[cur], nums[bound_2] = nums[bound_2], nums[cur]
            bound_2 -= 1
        else:
            cur += 1
