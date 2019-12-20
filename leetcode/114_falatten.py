"""
114、二叉树展开为链表
给定一个二叉树，原地将它展开为链表。
例如，给定二叉树,将其展开为链表(将right属性看作next)
"""
"""
观察：以前序遍历?
后续遍历：将根节点的右子树 挂在 根节点左子树的最右节点（不存在则该节点为其左节点）的下面
        将根节点的左子树 挂为 根节点的右子树
        （有种旋转的感觉）

要求原址：递归
    对根节点将其左子树
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left: # 后序遍历
            pre = root.left # 令 pre 指向左子树
            while pre.right:  # 找到左子树中的最右节点（不存在则该节点为其左节点）
                pre = pre.right
            pre.right = root.right # 令左子树中的最右节点的右子树 指向根节点的右子树
            root.right = root.left  # 令根节点的右子树指向根节点的左子树
            root.left = None  # 置空根节点的左子树





