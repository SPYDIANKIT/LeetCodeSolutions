# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Base case: if both nodes are None, they are the same
        if not p and not q:
            return True
        # If one of the nodes is None while the other is not, they are not the same
        elif not p or not q:
            return False
        # If node values are different, the trees are not the same
        elif p.val != q.val:
            return False
        # Recursively check left and right subtrees
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
