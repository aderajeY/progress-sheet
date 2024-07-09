# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return TreeNode(-1)

        curr_node = root

        while curr_node:
            if p.val < curr_node.val and q.val < curr_node.val:
                curr_node = curr_node.left
            elif p.val > curr_node.val and q.val > curr_node.val:
                curr_node = curr_node.right
            else:
                return curr_node

        return TreeNode(-1)
        