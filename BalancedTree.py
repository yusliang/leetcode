# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #isBalanced2, 两个返回值分别保存子树高度和子树是否平衡
        #depth, flag = self.isBalanced2(root)
        #return flag

        #isBalanced3, 返回值<0表示子树不平衡，否则表示子树的高度
        depth = self.isBalanced3(root)
        return depth >= 0
    def isBalanced2(self, root):
        if root is None:
            return (0, True)
        if root.left is None and root.right is None:
            return (1, True)
        if root.left is None and root.right is not None:
            depth, flag = self.isBalanced2(root.right)
            return (depth+1, flag and depth <= 1)
        if root.right is None and root.left is not None:
            depth, flag = self.isBalanced2(root.left)
            return (depth+1, flag and depth <= 1)
        ldepth, lflag = self.isBalanced2(root.left)
        rdepth, rflag = self.isBalanced2(root.right)
        return (max(ldepth+1, rdepth+1), lflag and rflag and abs(ldepth-rdepth) <= 1)
    def isBalanced3(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        ldepth = self.isBalanced3(root.left)
        rdepth = self.isBalanced3(root.right)
        if ldepth < 0 or rdepth < 0 or abs(ldepth-rdepth) > 1:
            return -2
        else:
            return max(ldepth,rdepth)+1
