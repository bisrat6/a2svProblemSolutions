class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for l in s:
            freq[l] = freq.get(l, 0) + 1
        
        # 1. Sort the (character, count) pairs from the dictionary items.
        #    The key is the count (value), sorted descending.
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        
        result = []
        # 2. Build the string by extending the list with the character repeated 'count' times.
        for char, count in sorted_items:
            result.extend([char] * count)
            
        return "".join(result)