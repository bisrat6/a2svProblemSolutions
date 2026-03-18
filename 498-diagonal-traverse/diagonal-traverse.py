class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        row = col = 0
        direction = 1  # 1 = up-right, -1 = down-left
        result = []

        for _ in range(m * n):
            result.append(mat[row][col])

            if direction == 1:  # going up-right
                if col == n - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1

            else:  # going down-left
                if row == m - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result