"""
102、二叉树的层次遍历

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        WHITE, GRAY = False, True
        init_level = 0
        stack = []
        res = []
        stack.append((root, WHITE, init_level))
        while stack:
            node, color, level = stack.pop()
            if node:
                if color == WHITE:
                    stack.append((node.right, WHITE, level + 1))
                    stack.append((node.left, WHITE, level+1))
                    stack.append((node, GRAY, level))
                else:
                    if len(res) == level:
                        res.append([])
                    res[level].append(node.val)
        return res

