# LeetCode算法归纳
在这里，对我的leetcode刷题进行总结与归纳，希望能够帮助自己更好的理解，也希望对别人也有所帮助，目前仅尝试了60多道leetcode题目，后续待补充
我将把这些题目按照解法类型进行分类，并尝试去总结每一种方法的流程  

## 动态规划
1. 还是要官方说法来一下
    >动态规划(dynamic programing)是运筹学的一个分支,是求解决策过程最优化的数学方法  
    >利用分阶段求解缩小决策问题的规模，  
    >利用分治策略将原问题分解为若干较小规模但类似于原问题的子问题  
    >自底向上  
2. 什么时候用动态规划
    >子问题有重叠，利用历史记录来记录  
    >常见问题：字符问题、矩阵问题  
3. 求解动态规划问题时的三个重要步骤
    - 定义数组dp的含义： dp[i][j]代表什么意思？
    - 找出数组之间的关系式：大部分情况下，dp[i] [j] 和 dp[i-1] [j]、dp[i] [j-1]、dp[i-1] [j-1] 肯定存在某种关系。
    - 找出初始值
4. 动态规划的优化策略
    >降低空间复杂度  
    >将二维数组降到一维（部分历史记录不会再被使用）  
5. 案例分析  
    稍后回来  
    
## 递归与回溯
1. 下定义
    >递归：通过重复将问题分解为同类的子问题而解决问题的方法。  
    >回溯：常用递归来进行，不同点：当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择  
    >递归的实现：函数栈  
    >递归算法的实质是把问题分解成规模缩小的同类问题的子问题，然后递归调用方法来表示问题的解。  
    >自顶向底  
2. 什么时候用递归或者回溯
3. 递归的三大要素：
    - 明确递归函数的功能是什么
    - 寻找递归的结束条件 （递归结束时，返回结果）
    - 找出函数的等价关系式 （不断缩小参数的范围）
4. 递归的优化思路：往DP发展
    > 是否有子问题被重复计算，利用hashmap来存储  
    > 考虑是否可以自底向上，改用动态规划  
5. 案例分析  
    稍后回来  
     
## 散列表Hashmap 
1. 下定义：
    >HashMap是一个用于存储Key-Value键值对的集合，每一个键值对也叫做Entry。  
    >具有关键字k的元素存放在槽h(k)中，利用散列函数h，由关键字k计算出槽的位置  
    >散列函数： index = hash(key) 通过hash函数，确定键key的位置  （要求散列函数近似的满足均匀散列假设）  
    >冲突：多个key对应同一个index    解决：在该index下存储一个链表，  
    - 高并发下HashMap的问题：  
        链表会形成链表环导致死循环为了安全 采用锁（判断链表有环，设置两个指针，具有不同步幅，套圈）  
        高并发下常采用 ConcurrentHashMap ：二级的hash
2. 什么时候使用hashmap
3. hashmap在Python中的表现形式：字典
    - key in dict: 如果键在字典 dict 里返回 true，否则返回 false。
    - dict.get(key,default=None) 返回指定键的值，如果值不在字典中返回默认值。
    - dict.popitem() 返回并删除字典最后的一个键值对
4. 案例
    - [1、两数之和](https://leetcode-cn.com/problems/two-sum/)    [解题](/leetcode/001_two_sum.py)
        >为了为了避免多次遍历，只需在num1之前的位置查找一遍即可  
        >用字典模拟哈希求解：逐个将num-index对放入字典里，在放进去之前先判断字典里是否有num2=target-nums[i]  
        >也可以利用列表的方法求解  
        ```Python
        def twoSum(self, nums, target):
            hash_map={}
            for index,num in enumerate(nums):
                if hash_map.get(target-num) is not None:
                    return [hash_map.get(target-num), index]
                hash_map[num] = index
        ```
        
## 滑动窗口
1. 下定义：
    >滑动窗口类型的题目经常是用来执行数组或是链表上某个区间（窗口）上的操作。比如找最长的全为1的子数组长度。    
    >滑动窗口一般从第一个元素开始，一直往右边一个一个元素挪动。  
    >当然了，根据题目要求，我们可能有固定窗口大小的情况，也有窗口的大小变化的情况。  
    >实现方法，双指针定窗口  
2. 什么时候需要上滑动窗口
    - 问题的输入是一些线性结构：比如链表呀，数组啊，字符串啊之类的  
    - 求最长/最短子字符串或是某些特定的长度要求  
3. 常见的问题：
    - 窗口大小为K的最大子数组和（简单）  
    - 拥有K个不同的字母的最长子串（中等） 
    - 字符串的同字母异序词（困难）
4. 案例
    - [3、无重复字符最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)  [解题](/leetcode/003_len_longestSubstring.py)
        >利用左右指针确定窗口边界  
        >右指针遍历列表，每当有一个新元素出现，判断窗口里是否已经有了该数据  
        >如果有，不满足条件，需要向右移动左指针，直到窗口不含有该新元素时将其加入  
        >需要记录窗口的当前长度和历史长度  
        ```Python
        def lengthOfLongestSubstring2(self, s: str) -> int:
            if not s: return 0
            left = 0
            max_len = 0
            cur_len = 0
            for right in range(len(s)):
                while s[right] in s[left:right]:
                    left += 1
                    cur_len -= 1
                cur_len += 1
                if cur_len > max_len: max_len = cur_len
            return max_len
        ```
              

## 其他题目
1. 链表题
    - [2、两数相加](https://leetcode-cn.com/problems/add-two-numbers/)  [题解](/leetcode/002_two_add.py)
        >链表常用方法：将新的链表挂在原先的某个链表下面  
        >在其中一个链表结束之后，剩下的一个链表衔接在其后即可  
        >如 两数相加 两个有序链表重排序等 
    
    - [4、寻找两个有序数组的中位数] (https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)  [题解](/leetcode/004_findMedianNum.py)
        >将数组AB分为两个部分 以(i+j = half_len = (m+n+1)//2 (左半部分比右半部分长1或0))  
        >使左半部分 A_left B_left 小于右半部分 A_right B_right 则中位数便可轻松找到 
        >使用二分法寻找i的位置， 缩减时间复杂度
        ```Python
        def findMedianSortedArrays(self, A, B):
            m, n = len(A), len(B)
            if m > n:  # 将较长的列表放在B的位置,这样只用考虑A的边界
                return self.findMedianSortedArrays(B, A)
            imin, imax, half_len = 0, m, (m+n+1)//2
            while imin < imax:
                i = imin + (imax-imin)//2
                j = half_len - i
                if A[i] < B[j-1]:
                    imin = i + 1
                else:
                    imax = i
            i = imin
            j = half_len - i
            max_of_left = max(A[i-1] if i > 0 else float("-inf"),
                              B[j-1] if j > 0 else float("-inf"))
            if (m+n)%2 == 1:
                return float(max_of_left)
            min_of_right = min(A[i] if i<m else float("inf"),
                               B[j] if j < n else float("inf"))
            return float((max_of_left+min_of_right)/2.0)
        ```

   
