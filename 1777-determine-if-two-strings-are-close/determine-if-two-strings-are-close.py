class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If lengths differ, impossible
        if len(word1) != len(word2):
            return False
        
        # Count frequencies of each character
        from collections import Counter
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        # 1) The sets of characters must match
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # 2) The sorted lists of frequencies must match
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True