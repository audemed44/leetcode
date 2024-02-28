# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = deque()
        current = root
        q.append(current)

        while q:
            current = q.popleft()
            if current.right:
                q.append(current.right)
            if current.left:
                q.append(current.left)
        
        return current.val
        