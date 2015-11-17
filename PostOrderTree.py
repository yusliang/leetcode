# -*- coding: cp936 -*-
class Solution(object):
    #�������ң�����ջ��ֱ�����֧ѭ�����ף���ʼ��ջ��
    #��ջʱ��������Һ��ӣ��Դ�Ϊ�����½��е�һ��
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
