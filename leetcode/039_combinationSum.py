"""
39、组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
	所有数字（包括 target）都是正整数。
	解集不能包含重复的组合。
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[  [7],
  [2,2,3]]
示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[  [2,2,2,2],
  [2,3,3],
  [3,5]]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解：
    回溯+剪枝  ：利用树形图来解决问题
    以target为根节点，对每一个分支做减法，减到0或负数的时候，剪枝，其中，减到0的时候结算。
    根结点到0 所经过的路径，加入结果集
    总结一下：在减的过程中，得到0 或者负数，就没有必要再走下去，
    所以这两种情况就分别表示成为叶子结点。此时递归结束，然后要发生回溯。
    问题：重复解：后面分支的更深层的边出现了前面分支低层的边的值。
    方法：排序，更深层的边上的数值不能比它上层的边上的数值小
"""

class Solution:
    def combinationSum(self, candidates, target) :
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        if target == 0:
            res.append(path[:])
        for index in range(begin, size):
            residue = target -candidates[index]
            if residue < 0:
                break
            path.append(candidates[index])
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()

    """
    回溯+剪枝
        以target为根节点，对每一个分支做减法，减到0或负数的时候，剪枝，
        其中，减到0的时候结算。负数的话则回到减法前的那一步（即回到其父亲节点，找另外的节点）
        
    """
    def combinationSum2(self, candidates, target):
        res = []
        n = len(candidates)
        if n == 0:
            return []
        path = []
        candidates.sort()   # 避免重复解
        def track_back(start, target):
            if target == 0:
                res.append(path[:])
            for i in range(start, n):
                residue = target - candidates[i]
                if residue < 0:
                    break
                path.append(candidates[i])  # 大于等与0的话，则将该节点加入路径
                track_back(i, residue)    # 因为每个数可以被重复使用，所以是i 不是i+1
                path.pop() # 当找到0的时候结算，回到其父亲节点
        track_back(0, target)
        return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    print(result)



