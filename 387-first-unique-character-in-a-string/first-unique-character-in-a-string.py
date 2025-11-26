from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count frequencies
        freq = Counter(s)
        
        # Find first character with freq 1
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
