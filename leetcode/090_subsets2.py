"""
90、子集2
不同与78之处，数组中含有重复元素
所以要注意重复的情况:
    注意如 [1, 2, 1] 则会产生[1,2] [2,1]等情况，
    所以要sort
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def track_back(index, tmp):
            if tmp not in res:
                res.append(tmp)
            for i in range(index, n):
                track_back(i+1, tmp + [nums[i]])
        track_back(0,[])
        return res