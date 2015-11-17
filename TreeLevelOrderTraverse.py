# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = [root]
        res = []
        while level and root:
            res.append([node.val for node in level])
            level = [kid for parent in level for kid in [parent.left, parent.right] if kid]
        res.reverse()
        return res
        #levelOrder2
        #res = []
        #self.levelOrder2(root, 0, res)
        #return res
    def levelOrder2(self, root, level, res):
        if root is not None:
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            self.levelOrder2(root.left, level+1, res)
            self.levelOrder2(root.right, level+1, res)
    
