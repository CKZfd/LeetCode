"""
221、最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
"""
"""
动态规划
    1、dp[i][j]: 以i，j作为右下角的最大正方形面积的边长
    2、关系：dp[i-1][j-1] 与dp[i][j]
        dp[i][j]为  [i][j]（包含）分别向左向上连续1的个数 （最多dp[i-1][j-1]+1个）      
    3、初始化：首行首列
优化：空间压缩
扩展到最大矩形：dp[i][j]  最大长宽
    不过要考虑面积的情况，好像要复杂挺多
    
题解：吴彦祖的答案
dp[i][j]表示以第iii行，第jjj列处为右下角的最大正方形的边长。
仅当该位置为111时，才有可能存在正方形。且递推公式为：
dp[i][j]=min(dp[i−1][j−1],dp[i−1][j],dp[i][j−1])+1。
含义为若当前位置为1，则此处可以构成的最大正方形的边长，是其正上方，左侧，和左上界三者共同约束的，且为三者中的最小值加1。

作者：zhu_shi_fu
链接：https://leetcode-cn.com/problems/maximal-square/solution/dong-tai-gui-hua-kong-jian-you-hua-zhu-xing-jie-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def maximalSquare(self, matrix) :
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        max_len = 0
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            max_len = max(max_len, dp[i][0])
        for j in range(1,n):
            dp[0][j] = int(matrix[0][j])
            max_len = max(max_len, dp[0][j])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
                    tmp = dp[i-1][j-1]
                    if tmp != 0:
                        for back_step in range(1,tmp+1):
                            if matrix[i][j - back_step] =="1" and matrix[i - back_step][j] == "1":
                                dp[i][j] += 1
                            else:
                                break
                    max_len = max(max_len, dp[i][j])
        return max_len*max_len

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        if (not matrix):
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        pre = 0
        dp = [0] * (n + 1)
        for i in range(0, m):
            for j in range(1, n + 1):
                tmp = dp[j]
                if (matrix[i][j - 1] == "1"):
                    dp[j] = min(pre, dp[j - 1], dp[j]) + 1
                    res = max(dp[j], res)
                else:
                    dp[j] = 0
                pre = tmp
            pre = 0
        return res * res


if __name__ == '__main__':
    s = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(s.maximalSquare(matrix))

