"""
142、环形链表2
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

a从表头走了n  b从表头走了2n 此时相遇说明 b比a多走了一个环的长度
    所以，环长是 n,
    设表头到环的入口为 m
    那么a再走m步 为 n+m 又一次回到了环的路口
    如何确定m，从表头从m步
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
