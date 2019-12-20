"""
160、相交链表
编写一个程序，找到两个单链表相交的起始节点。
如下面的两个链表：
"""
"""
题解：双指针
    假设两个链表长度不同， 分别为L1和L2，
    令两个指针A，B分别指向链表头节点处，行走L2步后B到达尾节点，
    此时A距离尾节点还有L1-L2，将B重新指向L1头节点，到A走到尾节点
  
    对于每一个指针：走完短（长）链表，再走长（短）链表  
     L1 = a+c L2 = b+c 其中c是两个链表的共有部分
    AB两指针走过的分别是 a+c+ b = b+c +a 同时到达交点处
注意程序的写法上是否能有改进
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha


