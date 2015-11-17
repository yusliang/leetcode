#Definition for a binary tree node.
# -*- coding: cp936 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                if not stack:
                    return res
                root = stack.pop()
                root = root.right
        return res

    #dum用来记录左分支到头时，下一个遍历的位置
    def morrisPreorderTraversal(self, root):
        res = []
        while root:
            res.append(root.val)
            if root.left:
                dum = root.left
                while dum.right:
                    dum = dum.right
                dum.right = root.right
                root = root.left
            else:
                root = root.right
        return res    
        
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
L= s.morrisPreorderTraversal(root)
print(L)
                
