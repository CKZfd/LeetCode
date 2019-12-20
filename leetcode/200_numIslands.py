"""
200、岛屿数量  c
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
mark 标记是否构成过其他岛屿，或者已经搜寻过的
递归：
    与79不同，mark只要构成其他的岛屿（1）或者已经被搜寻过（0），
        则，该点不会是一个新的岛屿
    遍历去寻找一个没有被寻找过的，且该点为1的点（新岛屿），
    递归的去寻找（在没有被寻找过的点）与该点构成同一岛屿的点，做上标记
参考题79：需要考虑回溯的情况，
"""
class Solution:
    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        island_num = 0
        mark = [[0]*n for i in range(m)]
        directs = [(0,1), (1,0), (0,-1), (-1,0)]

        def find_island_area(i,j):
            for direct in directs:
                cur_i, cur_j = i+direct[0], j+direct[1]
                if 0 <= cur_i and cur_i<m and 0<=cur_j and cur_j<n:
                    if mark[cur_i][cur_j] == 0:
                        mark[cur_i][cur_j] = 1
                        if grid[cur_i][cur_j] == "1":
                            find_island_area(cur_i,cur_j)


        for i in range(m):
            for j in range(n):
                # 不是别的岛屿的一部分  该点为1，则该点为一岛屿
                if mark[i][j] == 0:
                    mark[i][j] = 1 # 该点已经搜寻过
                    if grid[i][j] == "1":
                        island_num += 1
                        find_island_area(i,j) # 将与（i，j）组成同一片岛屿的点标记

        return island_num

if __name__ == '__main__':
    s = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(grid))
