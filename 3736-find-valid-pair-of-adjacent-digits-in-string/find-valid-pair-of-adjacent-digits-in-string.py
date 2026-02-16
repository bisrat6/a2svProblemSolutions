from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        
        for a, b in zip(s, s[1:]):
            if (
                a != b and
                freq[a] == int(a) and
                freq[b] == int(b)
            ):
                return a + b
        
        return ""
