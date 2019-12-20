"""
22、括号生成
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解：
    观察：左右括号数一样，头尾分别是左右括号
         如果前面左右括号数一致，则剩下的部分依然服从上述规律 -> 动态规划 + mapping
    n对括号 可以分为以下两种情况 （）+n-1对括号   （ n-1对括号 ）
    动态规划：自底向上 从1到n 对括号的记录
        在求N个括号的排列组合时，把第N种情况（也就是N个括号排列组合）
        视为单独拿一个括号E出来，剩下的N-1个括号分为两部分，
        P个括号和Q个括号，P+Q=N-1，然后这两部分分别处于括号E内和括号E的右边，
        各自进行括号的排列组合。
    由于我们是一步步计算得到N个括号的情况的，所以小于等于N-1个括号的排列组合方式我们是已知的
    （用合适的数据结构存储，方便后续调用，且在存储时可利用特定数据结构实现题目某些要求，
    如排序，去重等），且P+Q=N-1，P和Q是小于等于N-1的，
    所以我们能直接得到P个和Q个括号的情况，进而得到N个括号的结果！
https://leetcode-cn.com/problems/generate-parentheses/solution/zui-jian-dan-yi-dong-de-dong-tai-gui-hua-bu-lun-da/
"""
class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
        total_l = []
        total_l.append([None])  # 0组括号时记为None
        total_l.append(["()"])  # 1组括号只有一种情况
        for i in range(2, n + 1):  # 开始计算i组括号时的括号组合
            l = []
            for j in range(i):  # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]  # p = j 时的括号组合情况
                now_list2 = total_l[i - 1 - j]  # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        # 前面设0的意义，这里k1,k2分别为0时代表两种情况
                        el = "(" + k1 + ")" + k2
                        l.append(el)  # 把所有可能的情况添加到 l 中
            total_l.append(l)  # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]




if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.generateParenthesis(3))