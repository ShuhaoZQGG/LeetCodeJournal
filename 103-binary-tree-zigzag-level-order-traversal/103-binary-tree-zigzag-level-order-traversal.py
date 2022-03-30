# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if root is None:
        return []
      res = []
      s1 = [root]
      s2 = []
      level = []
      while s1 or s2:
        while s1:
          root = s1.pop()
          level.append(root.val)
          if root.left:
            s2.append(root.left)
          if root.right:
            s2.append(root.right)
        if level:
          res.append(level)
        level = []
        while s2:
          root = s2.pop()
          level.append(root.val)
          if root.right:
            s1.append(root.right)
          if root.left:
            s1.append(root.left)
        if level != []:
          res.append(level)
        level = []
      return res