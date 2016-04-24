#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right
        #Recursive 
        #res = []
        #self.inorder(root, res)
        return res
    def morrisInorder(self, root):
        res = []
        while(root):
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                dum = root.left
                while(dum.right and dum.right != root):
                    dum = dum.right
                if not dum.right:
                    dum.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    root = root.right
        return res
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
print(s.morrisInorder(root))

    
