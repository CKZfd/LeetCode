"""
40、组合总和
给定一个数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。
"""
"""
与题39的不同之处：
    1、数组的元素可能有重复
    2、要求：每个元素在每个组合中只能使用一次

题解：回溯+剪枝
    以target为根节点，对每一个分支做减法，直到<=0
    根节点到叶子节点为0的路径加入解集
    不重复：先排序
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if n == 0:
            return []
        res = []
        path = []
        candidates.sort()
        def track_back(start,target):
            if target == 0 and path not in res: # 避免重复解
                res.append(path[:])
            for i in range(start,n):
                residue = target - candidates[i]
                if residue < 0:
                    break
                path.append(candidates[i])
                track_back(i+1, residue)
                path.pop()
        track_back(0,target)
        return res
