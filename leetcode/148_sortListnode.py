"""
148、链表排序
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
"""
"""
归并排序：
    采用分治法，使每个子序列有序 (递归)
    步骤1：把长度为n的输入序列分成两个长度为n/2的子序列；
    步骤2：对这两个子序列分别采用归并排序；
    步骤3：将两个排序好的子序列合并成一个最终的排序序列。
    时间复杂度 O(n logn)
对于链表：
    1、分割 找到当前链表的中点：快慢指针找中点，找到后切割开
        分割递归的终止情况 head.next = None
    2、合并环节 将两个排序链表合并为一个有序链表
        双指针合并法
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 终止条件
        if not (head and head.next):
            return head
        # 寻找中点,并切割
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        # 递归进行分割
        left, right = self.sortList(head), self.sortList(mid)
        # 合并环节
        h = res = ListNode(0) # 创建一个无意义的表头，便于排序
        while left and right:
            if left.val <= right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right # 当有一个遍历完了，把另一个直接接在后面即可
        return res.next