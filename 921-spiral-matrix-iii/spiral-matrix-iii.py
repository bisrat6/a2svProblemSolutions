class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        result = []
        steps = 1
        r, c = rStart, cStart
        
        # directions: right, down, left, up
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        d = 0  # direction index
        
        while len(result) < rows * cols:
            for _ in range(2):  # repeat twice before increasing steps
                dr, dc = dirs[d]
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    r += dr
                    c += dc
                d = (d + 1) % 4
            steps += 1
        
        return result