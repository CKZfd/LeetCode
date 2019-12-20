"""
19、删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
题解：
1、确定链表的长度， 删除的节点为第L-n+1个节点
2、双指针，间隔n, 在寻找到尾节点时恰好找到被删除节点的上一个元素
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 增加一个特殊节点方便边界判断
        p = ListNode(-1)
        p.next, a, b = head, p, p
        while n > 0 and b:
            b, n = b.next, n-1
        if not b:
            return head
        while b.next:
            a, b = a.next, b.next
        a.next = a.next.next
        return p.next

