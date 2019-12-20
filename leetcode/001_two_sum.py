"""
1、两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
解题思路：
    用字典模拟哈希求解, 为了避免多次遍历，只需在num1之前的位置查找一遍即可
        初步方法：将所有的num-index对放入字典里，循环取出num1，再去判断num2是否再字典中
        改进：逐个将num-index对放入字典里，在放进去之前先判断字典里是否有num2
        字典的get用法 dict.get(key, default=None)
        参数 key -- 字典中要查找的键。 default -- 如果指定键的值不存在时，返回该默认值。
        返回值 返回指定键的值，如果值不在字典中返回默认值None。
    较慢的方法LIst
        num2 in nums，返回 True 说明有戏
        nums.index(num2)，查找 num2 的索引
"""
class Solution:
    def twoSum(self, nums, target):
        hash_map={}
        for index,num in enumerate(nums):
            if hash_map.get(target-num) is not None:
                return [hash_map.get(target-num), index]
            hash_map[num] = index

    def twoSum_list(self, nums, target):
        j = -1
        for i in range(len(nums)):
            temp = nums[:i]
            if (target-nums[i]) in temp:
                j = temp.index(target-nums[i])
                break
        if j>=0:
            return [j,i]




if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))