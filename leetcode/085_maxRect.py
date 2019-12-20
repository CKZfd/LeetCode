"""
85、最大矩形
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
示例:
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
动态规划
    1、定义数组dp[][]的含义：dp[i][j] = (row, line, area)
        row:当前位置向左连续1的个数
        line: 当前位置向上连续1的个数
        area: 当前位置能构造的最大矩形面积
    2、数组元素之间的关系式
        if M[i][j] == 1: 
            dp[i][j][0] = dp[i][j-1][0] + 1
            dp[i][j][1] = dp[i-1][j][1] + 1
            面积需要画图考虑，遍历line的宽
        M[i][j] == 0:
            max
    3、找出初始值：
        dp[0][0] = (0,0,0) or (1,1,1)
        第一行:
        第一列
        
"""
class Solution:
    def maximalRectangle(self, matrix) :
        m, n = len(matrix), len(matrix[0])
        dp_row = [[0]*n for i in range(m)]
        dp_line = [[0]*n for i in range(m)]
        dp_area = [[0] * n for i in range(m)]

        if not matrix:
            return 0
        if matrix[0][0] == "1":
            dp_row[0][0], dp_line[0][0], dp_area[0][0] = 1, 1, 1
        else:
            dp_row[0][0], dp_line[0][0], dp_area[0][0] = 0, 0, 0
        for i in range(1, m):
            if matrix[i][0] == "1":
                dp_row[i][0] = dp_row[i-1][0] + 1
                dp_line[i][0] = 1
                dp_area[i][0] = max(dp_area[i-1][0], dp_row[i][0])
            else:
                dp_row[i][0], dp_line[i][0], dp_area[i][0] = 0, 0, dp_area[i-1][0]

        for j in range(1, n):
            if matrix[0][j] == "1":
                dp_row[0][j] = 1
                dp_line[0][j] = dp_line[0][j-1] + 1
                dp_area[0][j] = max(dp_area[0][j-1], dp_line[0][j])
            else:
                dp_row[0][j], dp_line[0][j], dp_area[0][j] = 0, 0, dp_area[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                cur_max = 0
                if matrix[i][0] == "1":
                    dp_row[i][j] = dp_row[i-1][j] + 1
                    dp_line[i][j] = dp_line[i][j-1] + 1
                    for t in range(dp_line[i][j]):
                        cur_max = max(cur_max, dp_line*dp_row)


    def maximalRectangle2(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        #将每一行看作一个二进制数，然后转化为一个整数
        nums = [int(''.join(row), base=2) for row in matrix]
        ans, N = 0, len(nums)
        #遍历所有行
        for i in range(N):
            j, num = i, nums[i]
            #将第i行，连续的，和接下来的所有行，做与运算
            while j < N:
                #经过与运算后，num转化为二进制中的1，表示从i到j行，可以组成一个矩形的那几列
                num = num & nums[j]
                if not num:
                    break
                l, curnum = 0, num
                #这个循环最精彩
                #每次循环将curnum和其左移一位的数做与运算
                #最终的循环次数l表示，最宽的有效宽度，
                while curnum:
                    l += 1
                    curnum = curnum & (curnum << 1)
                ans = max(ans, l * (j - i + 1))
                j += 1
        return ans


if __name__ == '__main__':
    # begin
    s = Solution()
    s1 = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

    print(s.maximalRectangle2(s1))
