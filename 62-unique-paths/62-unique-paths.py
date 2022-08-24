class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def findPaths(m, n):
            if m == 1 or n == 1:
                return 1
            else:
                return findPaths(m, n - 1) + findPaths(m - 1, n)
        return findPaths(m, n)