"""
4、寻找两个有序数组的中位数
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
中位数：将一个集合划分为两个长度相等的子集，其中一个子集中的元素总是大于另一个子集中的元素。
注意：奇偶
将A和B各自划分为左右两个部分（i，j），什么时候找到中位数,
    奇数个：len(left)=len(right)+1
    偶数个：len(left)=len(right)
    且A[i-1]<=B[j]  and B[j-1]<=A[i]  （左半部分总是小于右半部分）
    注意遇到边界

解法：总是将较长的列表放在B的位置
对A使用二分法寻找i的位置，判断A[i] 与 B[j-1]的关系
那么j的位置自然确定 j = half_len - i 
时间复杂度：O(log(min(m,n)))
"""


class Solution:
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:  # 将较长的列表放在B的位置,这样只用考虑A的边界
            return self.findMedianSortedArrays(B, A)
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin < imax:
            i = imin + (imax-imin)//2
            j = half_len - i
            if A[i] < B[j-1]:
                imin = i + 1
            else:
                imax = i
        i = imin
        j = half_len - i
        max_of_left = max(A[i-1] if i > 0 else float("-inf"),
                          B[j-1] if j > 0 else float("-inf"))
        if (m+n)%2 == 1:
            return float(max_of_left)
        min_of_right = min(A[i] if i<m else float("inf"),
                           B[j] if j < n else float("inf"))
        return float((max_of_left+min_of_right)/2.0)








if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findMedianSortedArrays( [2,3,6],[]))
