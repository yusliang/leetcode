# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


##重点在于，判断是否是树叶不需要判断是否没有左右孩子，而是只要是none就说明到头了
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
        		return 0
        l = maxDepth(self, root.left)
        r = maxDepth(self, root.right)
        return (max(l, r) + 1)		
        				
        
      	"""calcDepth(self, root, 0, 0)
      	
    def calcDepth(self, node, depth, max_depth):
    		if node.left == None and node.right == None:
    				if depth > max_depth:
    						return depth
    				else:
    						return max_depth
    		elif node.left == None:
  					m1 = calcDepth(self, node.right, depth + 1, max_depth)		
    		elif node.right == None:
    				m2 = calcDepth(self, node.left, depth + 1, max_depth)
    		else:
    				m1 = calcDepth(self, node.left, depth + 1, max_depth)
    				m2 = calcDepth(self, node.right, depth + 1, max_depth)
    		return max(m1, m2)
    		"""
        