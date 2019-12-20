#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    排序算法
    升序
    包括：
"""

# 冒泡排序
def bubbleSort(seq):
    """
        1、遍历一轮，比较相邻元素,将最大的移到最后一位(冒泡，将最大的元素一直后移)
        2、执行n-1轮，则只剩下一个最小的元素处在第一个位置
        时间复杂度 O(n^2)
    """
    for i in range(len(seq)-1):  # 最后一个元素自然确定
        for j in range(len(seq)-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq


# 选择排序
def selectSort(seq):
    """
        原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
        然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
        以此类推，直到所有元素均排序完毕。
        时间复杂度 O(n^2)
    """
    for i in range(len(seq)-1):   # 最后一个元素自然确定
        minIndex = i
        for j in range(i+1,len(seq)):
            if seq[minIndex] > seq[j]:
                minIndex = j
        seq[i], seq[minIndex] = seq[minIndex], seq[i]
    return seq


# 插入排序
def insertSort(seq):
    """
    原理：通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，
        找到相应位置并插入。
        时间复杂度 O(n^2)
    """
    for j in range(1, len(seq)): # 只有一个的序列是有序的
        key = seq[j]
        i = j - 1
        while i >= 0 and key < seq[i]:
            seq[i+1] = seq[i]
            i -= 1
        seq[i+1] = key
    return seq


# 希尔排序
def shellSort(seq):
    """
    希尔排序，插入排序的改进，也称为缩小增量排序， 优先比较距离较远的元素
    希尔排序按一定增量分组，对每组使用直接插入排序算法排序；
    随着增量逐渐减少，每组包含的关键词越来越多，
    当增量减至1时，整个文件恰被分成一组，算法便终止。
    时间复杂度 O(n logn)
    """
    n = len(seq)
    gap = n//2
    while gap >= 1:
        for i in range(gap,n):  # 从每组的第二个元素开始（插入排序）
            key = seq[i]
            preIndex = i - gap
            while preIndex >= 0 and key < seq[preIndex]:
                seq[preIndex + gap] = seq[preIndex]
                preIndex -= gap
            seq[preIndex + gap] = key
        gap //= 2
    return seq


# 归并排序
"""
    采用分治法，使每个子序列有序 (递归)
    步骤1：把长度为n的输入序列分成两个长度为n/2的子序列；
    步骤2：对这两个子序列分别采用归并排序；
    步骤3：将两个排序好的子序列合并成一个最终的排序序列。
    时间复杂度 O(n logn)
"""
# 将两段排序好的数组结合成一个排序数组
def merge(left, right):
    i = j = 0
    c = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            c.append(left[i])
            i += 1
        else:
            c.append(right[j])
            j += 1
    if i == len(left):
        while j < len(right):
            c.append(right[j])
            j += 1
    else:
        while i < len(left):
            c.append(left[i])
            i += 1
    return c


def mergeSort(seq):
    if len(seq) == 1:  # 注意，递归要有返回和终止条件
        return seq
    mid = len(seq)//2
    left = mergeSort(seq[:mid])
    right = mergeSort(seq[mid:])
    return merge(left, right)


# 快速排序
"""
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）
分为较小和较大的2个子序列，然后递归地排序两个子序列。 
步骤为： 挑选基准值：从数列中挑出一个元素，称为"基准";
分割：重新排序数列，所有比基准值小的元素摆放在基准前面，
    所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。
    在这个分割结束之后，对基准值的排序就已经完成;
递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
另有一种哨兵法，左右各置一哨兵，key=A[0] i,j = low+1, high 
    从j开始往前搜索到第一个小于key的值, A[i]A[j]交换
    从i开始往后。。。
    重复直到i>=j， 交换key与A[j]
"""
def partition(seq, low, high):
    i = low
    key = seq[high]
    for j in range(low, high):
        if seq[j] <= key:
            seq[i], seq[j] = seq[j], seq[i]
            i += 1
    seq[i], seq[high] = seq[high], seq[i]
    return i


def q_sort(seq, left, right):
    if left < right:
        pivot = partition(seq, left, right)
        q_sort(seq, left, pivot-1)
        q_sort(seq, pivot + 1, right)
    return seq


def quickSort(seq):
    return q_sort(seq, 0, len(seq)-1)


# quick sort 百度百科易理解版
def quicksort(seq):
    if len(seq) < 2:  # 基线条件（停止递归的条件）
        return seq
    else:  # 递归条件
        baseValue = seq[0]  # 选择基准值
        #由所有小于基准值的元素组成的子数组
        less = [m for m in seq[1:] if m < baseValue]
        #包括基准在内的同时和基准相等的元素，
        equal = [w for w in seq if w == baseValue]
        #由所有大于基准值的元素组成的子数组
        greater = [n for n in seq[1:] if n > baseValue]
        return quickSort(less) + equal + quickSort(greater)


# 堆排序
"""
    排序步骤：1、建立最大堆 
    2、从后向前循环，exchange seq[0] seq[i-1] 将(根节点)最大值放置队尾,并缩小堆，使该值不在堆中，
    3、调用max_heapify(seq, 1, heap_size) 重新将堆调整为最大堆
    建立最大堆步骤： 从底至上对每一个根节点去进行max_heapify,使每一个节点满足根节点最大的需求
    max_heapify 递归的从A[i] A[LEFT(i)] A[RIGHT(i)] 里取最大，使得较小的节点一直下沉
"""
# python列表从0开始， 堆节点从1开始
# 递归的从A[i] A[LEFT(i)] A[RIGHT(i)] 里取最大，使得较小的节点一直下沉
def max_heapify(seq, i, heap_size):
    l = i << 1
    r = (i << 1) + 1
    largest = i
    if l <= heap_size and seq[largest-1] < seq[l-1]:
        largest = l
    if r <= heap_size and seq[largest-1] < seq[r-1]:
        largest = r
    if largest != i:
        seq[i-1], seq[largest-1] = seq[largest-1], seq[i-1]
        max_heapify(seq, largest, heap_size)


# 从底至上对每一个根节点去进行max_heapify,使每一个节点满足根节点最大的需求
# 可以在线性时间内将一个无序数组构建成最大堆
def build_max_heap(seq):
    heap_size = length = len(seq)
    for i in range(length//2, 0, -1):
        max_heapify(seq, i, heap_size)


def heapSort(seq):
    build_max_heap(seq)
    heap_size = length = len(seq)
    for i in range(length, 1, -1):
        seq[0], seq[i-1] = seq[i-1], seq[0]  # 最大值放置队尾,并缩小堆，使该值不在堆中
        heap_size -= 1
        max_heapify(seq, 1, heap_size)
    return seq





if __name__ == '__main__':
    seq = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    seq = heapSort(seq)
    print(seq)
