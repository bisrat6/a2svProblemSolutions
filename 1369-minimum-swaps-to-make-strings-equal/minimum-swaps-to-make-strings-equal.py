class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Count mismatches of type 'xy' and 'yx'
        xy = 0
        yx = 0
        
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
        
        # Swaps count
        swaps = 0
        
        # Each two xy mismatches can be solved in 1 swap
        swaps += xy // 2
        xy %= 2
        
        # Same for yx mismatches
        swaps += yx // 2
        yx %= 2
        
        # If both have leftover 1 mismatch each, we need 2 more swaps
        if xy == 1 and yx == 1:
            swaps += 2
        
        # If one is leftover but not the other, it's impossible
        elif (xy + yx) % 2 == 1:
            return -1
        
        return swaps