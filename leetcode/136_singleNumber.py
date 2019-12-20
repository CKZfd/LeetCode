"""
136、只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
1、haspmap   hashmap.popitem()[0]
2、位操作 异或操作
"""

class Solution:
    def singleNumber(self, nums):
        hashmap = {}
        for num in nums:
            if num in hashmap.keys():
                del hashmap[num]
            else:
                hashmap[num] = num
        return hashmap.popitem()[0]

    def singleNumber2(self, nums):
        a = 0
        for num in nums:
            a ^= num
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 1, 2, 4, 1]))