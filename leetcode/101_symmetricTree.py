"""
101、对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
"""
"""
递归+双指针
要递归的比较左子树和右子树。
结束条件
镜像对称:
    1、两个指针当前节点对称
    2、A的右子树与B的左子树对称
    3、A的左子树与B的右子树对称
    
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def isMirror(t1, t2):
            if not (t1 or t2):
                return True
            if not (t1 and t2):
                return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
        return isMirror(root.left, root.right)