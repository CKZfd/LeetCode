"""
169、多数元素
给定一个大小为 n 的数组，找到其中的多数元素。
多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ （向下取整）的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
1、hashmap 
2、排序后，因为多数元素出现次数多于⌊ n/2 ⌋ 
    其必然出现再nums[⌊ n/2 ⌋]处
    但不过排序的时间复杂度 为 nlogn
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = n//2
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            if hashmap[num] > m:
                return num
        return



    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
