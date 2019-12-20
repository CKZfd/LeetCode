"""
2、两数相加
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，
并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解
注意：链表操作
     python3的整除为 //
循环遍历两个链表，为了避免空间占用，将返回的链表p挂在链表l1下，
每次遍历都将链表a和链表b的值相加，再赋给链表a。 
如果有进位我们还需要记录一个进位标志。
当循环结束时，如果进位标志>0还需要处理下边界条件。
我们不用生成一个新的节点，直接将两个节点相加的值赋给节点a就可以了，
循环的结束条件是链表ab都为空，这样当整个循环结束时，链表就被串起来了。

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        # 用a,b指向l1,l2的表头，
        a, b, p, carry = l1, l2, None, 0
        while a or b:
            # a和b节点的值相加，如果有进位还要加上进位的值
            val = (a.val if a else 0) + (b.val if b else 0) + carry
            # 判断val是否有进位
            carry, val = val//10, val%10
            # 链表p指向a的位置
            p, p.val = a if a else b, val
            a, b = a.next if a else None, b.next if b else None
            # 遍历完a之后，将b链表的后续部分挂在a的后面
            p.next = a if a else b
        if carry:
            p.next = ListNode(carry)
        # 每次迭代实际上都是将val赋给a指针的，所以最后返回的是l1
        return l1