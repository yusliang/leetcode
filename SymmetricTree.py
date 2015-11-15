# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetric2(root.left, root.right)
    def isSymmetric2(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val==right.val and self.isSymmetric2(left.left, right.right) and self.isSymmetric2(left.right, right.left)
        
