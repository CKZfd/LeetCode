"""
105、从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。
例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
前序：父节点、左节点、右节点
中序：左节点、父节点、右节点
    前序遍历的第一个元素为根节点，
    而在后序遍历中，该根节点所在位置的左侧为左子树，右侧为右子树。
构建二叉树的问题本质是：
    1、找到各个子树的根节点 root
    2、构建该根节点的左子树
    3、构建该根节点的右子树
递归
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # 找到根节点在中序遍历的索引
        # 对于中序遍历而言，mid之前为其左子树的中序，mid之后为其右子树的遍历
        # 子树的遍历序列长度一致，第一个为根节点的值
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


