"""
48、旋转图像
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
找规律:即:任意一个(i,j) , (j, n-i-1), (n-i-1, n-j-1), (n -j-1, i)
    就是这四个索引号上的数交换.
翻转
直接举例子:
翻转整个数组,再按正对角线交换两边的数    
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] = \
                    matrix[n - j - 1][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]

        def rotate2(self, matrix: List[List[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            n = len(matrix)
            matrix[:] = matrix[::-1]
            # print(matrix)
            for i in range(0, n):
                for j in range(i + 1, n):
                    # print(i, j)
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
