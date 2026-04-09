from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers):
        count = Counter(answers)
        res = 0
        
        for x, freq in count.items():
            group_size = x + 1
            groups = ceil(freq / group_size)
            res += groups * group_size
        
        return res