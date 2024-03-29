# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        maximum, minimum = math.inf, -math.inf
        stack = [(root, maximum, minimum)]
        while stack:
            node, high, low = stack.pop()
            if not node:
                continue
            if node.val >= high or node.val <= low:
                return False
            stack.append((node.left, node.val, low))
            stack.append((node.right, high, node.val))
        return True
            