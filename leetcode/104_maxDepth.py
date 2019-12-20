"""
104、二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
"""
"""
利用层次遍历（shen度搜索）,记录深度
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        WHITE, GRAY = 0, 1
        max_depth = 0
        depth = 1
        stack = [(WHITE, root, depth)]
        while stack:
            color, node, depth = stack.pop()
            if node:
                if color == WHITE:
                    stack.append((WHITE, node.right, depth+1))
                    stack.append((GRAY, node, depth))
                    stack.append((WHITE, node.left, depth+1))
            else:
                max_depth = max(max_depth, depth-1)
        return max_depth

