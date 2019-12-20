"""
206、反转链表
反转一个单链表。
"""
"""
递归啊
2、利用递归 + 双指针的方法
    递归时返回两个指针，一个指向反转部分的链表头，一个指向反转部分的链表尾
        方便将上一个元素衔接在其后面，形成反转
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur

    def reverseList2(self, head: ListNode) -> ListNode:
        def helper(head):
            if head == None or head.next == None:
                return head, head   # 当条件。。，头尾两个指针都指向head
            pre, last = helper(head.next)
            last.next = head # 链表的尾指针下一个是head
            head.next = None # 避免链表循环
            return pre, head   # 返回反转部分的头尾两个指针

        rt, _ = helper(head)
        return rt

