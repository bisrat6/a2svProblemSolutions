class Solution:
    def combine(self, n: int, k: int):
        result = []
        comb = []
        
        def backtrack(start):
            # If the current combination is of size k, add a copy to result
            if len(comb) == k:
                result.append(comb[:])
                return
            
            # Try all possible next numbers
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()
        
        backtrack(1)
        return result