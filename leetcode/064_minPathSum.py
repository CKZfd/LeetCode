"""
64、最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，
使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
动态规划：
    1、定义数组dp[i][j]含义: 到达网格位置（i, j）路径上的最小数字总和
    2、找出数组元素之间的关系式 dp[i][j]= min( dp[i-1][j], dp[i][j-1] ) + arr[i][j]
        到达位置（i, j）路径上的数字总和有两种：
            一种是位置（i-1, j）路径上的数字总和 + 位置（i, j）上的数字
            一种是位置（i, j-1）路径上的数字总和 + 位置（i, j）上的数字
    3、找出初始值：
        dp[0][0] = arr[0][0]
        第一行： dp[0][j] = dp[0][j-1] + arr[0][j]
        第一列：dp[i][0] = dp[i-1][0] + + arr[i][0] 
改进：
    原址操作，直接在grid上进行操作，无需再创建新的DP
    原grid 矩阵元素中被覆盖为dp 元素后（都处于当前遍历点的左上方），不会再被使用到。
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if not i and not j:
                    continue
                elif not i:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif not j:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

