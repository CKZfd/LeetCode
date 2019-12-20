"""
207、课程表
现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
课程安排是否为有向无环图DAG ， 课程间有前置条件，若出现环路，前置条件不成立
方法：拓扑排序 判断课程安排表是否为有向无环图DAG
    拓扑排序是对 DAG 的顶点进行排序，使得对每一条有向边 (u,v)，
    均有u（在排序记录中）比v先出现。
    亦可理解为对某点v而言，只有当v的所有源点均出现了，v才能出现。
需要：邻接矩阵，可由课程安排前置条件列表生成

1、借由入度表实现贪心：
    1、生成入度表
    2、将入度为0的节点入队
    3、依次将入度为0的的节点出队：删除该节点的顶点和所有以它为起始点的有向边
        实现：将与该节点邻接的节点的入度-1
    重复2，3
2、深度优先遍历 DFS 递归
    1、每个节点做标记 判断是否被遍历过  列表（颜色标记的变形）
        未被 DFS 访问：i == 0；
        已被其他节点启动的DFS访问：i == -1；
        已被当前节点启动的DFS访问：i == 1。
    2、对每个节点依次执行DFS，判断每个节点的DFS是否存在环：
        当 flag[i] == -1，说明当前访问节点已被其他节点启动的 DFS 访问，
            无需再重复搜索，直接返回 TrueTrueTrue。
        当 flag[i] == 1，说明在本轮 DFS 搜索中节点 i 被第 2 次访问，
            即 课程安排图有环，直接返回 FalseFalseFalse。
    将当前访问节点 i 对应 flag[i] 置 1，即标记其被本轮 DFS 访问过；
    递归访问当前节点 i 的所有邻接节点 j，当发现环直接返回 False；
    当前节点所有邻接节点已被遍历，并没有发现环，则将当前节点 flag 置为 −1 并返回 True。

"""

class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0]*numCourses
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        # cur, pre 分别为课程及其前置课程，当前课程由前置课程进入
        for cur,pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        for i in range(len(indegrees)):
            if not indegrees[i]:  # 将入度为0的节点入队
                queue.append(i)
        # BFS topsort
        while queue:
            pre = queue.pop(0)
            numCourses -= 1   # 节点数目减1
            for cur in adjacency[pre]: # 删除入度0的节点和以它为起始点的有向边
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses # 如果所有节点都被去除，该图无环

    def canFinish2(self, numCourses, prerequisites):
        adjacency = [[] for _ in range(numCourses)]
        flags = [0]*numCourses
        for cur,pre in prerequisites:
            adjacency[pre].append(cur)
        def dfs(i):
            if flags[i] == -1: # 已经被别的点遍历过，无环
                return True
            if flags[i] == 1: # 有环
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses): # 对每一个节点进行DFS，判断其是否无环
            if not dfs(i):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1,0], [0,1]]))
