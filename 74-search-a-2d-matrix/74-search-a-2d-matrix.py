class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      top, bot = 0, len(matrix) - 1
      while top <= bot:
        midRow = (top + bot) // 2
        if matrix[midRow][0] > target:
          bot = midRow - 1
        elif matrix[midRow][-1] < target:
          top = midRow + 1
        else:
          break
          
      if top > bot:
        return False
      
      left, right = 0, len(matrix[0]) - 1
      
      while left <= right:
        middle = (left + right) // 2
        if matrix[midRow][middle] == target:
          return True
        elif matrix[midRow][middle] < target:
          left = middle + 1
        else:
          right = middle - 1
      
      return False