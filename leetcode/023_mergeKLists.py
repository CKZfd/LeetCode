"""
23、合并k个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
根据合并两个有序链表的思想，先将每个链表都转换为列表，
然后将这些列表合并排序，最后再将排序后的列表转换为Listnode，简单易懂
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def transfer(self, a:ListNode):
        b = []
        while a:
            b.append(a.val)
            a= a.next
        return b

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        S = []
        for a in lists:
            b = self.transfer(a)
            for num in b:
                S.append(num)
        if len(S) == 0:
            return ListNode("")
        S.sort()
        first = S.pop(0)
        result = ListNode(first)
        node = result
        for n in S:
            node.next = ListNode(n)
            node = node.next
        return result

