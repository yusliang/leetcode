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
    #按根，右，左入栈，直到左分支循环到底，开始出栈。
    #出栈时，如果是右孩子，以此为根重新进行第一步
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [], []
        flag = True
        while True:
            if root and flag:
                stack.append((root, False))
                if root.right:
                    stack.append((root.right, True))
                root = root.left
            else:
                if not stack:
                    return res
                root, flag = stack.pop()
                if not flag:
                    res.append(root.val)
        return res
    
    def postorderTraversal2(self, root):
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.right
            if not stack:
                return res[::-1]
            root = stack.pop()
            root = root.left
        
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
L= s.postorderTraversal2(root)
print(L)
                
