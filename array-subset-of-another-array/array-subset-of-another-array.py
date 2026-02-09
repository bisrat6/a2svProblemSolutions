from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        ca = Counter(a)
        cb = Counter(b)
    
        for k in cb:
            if cb[k] > ca[k]:
                return False
        return True