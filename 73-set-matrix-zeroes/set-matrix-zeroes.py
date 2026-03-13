class Solution:
    def setZeroes(self, matrix):
        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

        # first pass
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # second pass
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0