# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative: BFS Level Order 
        if not root:
            return []
        
        queue = deque()
        traversal = []
        queue.append(root)

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            traversal.append(level[-1]) # Append rightmost node.

        return traversal

        # O(n) time.
        # O(n) auxiliary space.
        # O(n) total space.