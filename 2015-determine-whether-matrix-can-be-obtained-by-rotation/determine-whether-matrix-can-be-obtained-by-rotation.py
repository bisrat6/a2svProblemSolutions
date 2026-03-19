class Solution:
    def findRotation(self, mat, target):
        def rotate(matrix):
            return [list(row)[::-1] for row in zip(*matrix)]
        
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False