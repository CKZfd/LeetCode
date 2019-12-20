"""
79、单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解：回溯+剪枝
同一个单元格内的字母不允许被重复使用。：需要标记是否使用过
1、遍历：寻找和word第一个字母相同的点，作为深搜的根节点
2、每一个点上下左右试探，是的话以该节点作为
注意回溯
"""

class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        if m == 0:
            return not word
        mark = [[0]*n for i in range(m)]
        directs = [(0,1), (1,0), (0,-1), (-1,0)]
        def track_back(i,j,word):
            if len(word) == 0:
                return True
            for direct in directs:
                cur_i = i + direct[0]
                cur_j = j + direct[1]
                if 0<=cur_i and cur_i<m and 0<=cur_j and cur_j<n:
                    if mark[cur_i][cur_j] == 1:
                        continue
                    if board[cur_i][cur_j] == word[0]:
                        mark[cur_i][cur_j] = 1
                        if track_back(cur_i,cur_j,word[1:]):
                            return True
                        else: # 回溯
                            mark[cur_i][cur_j] = 0
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if track_back(i, j, word[1:]):
                        return True
                    else: # 回溯
                        mark[i][j] = 0
        return False


if __name__ == '__main__':
    s = Solution()
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word = "AAB"
    print(s.exist(board, word))