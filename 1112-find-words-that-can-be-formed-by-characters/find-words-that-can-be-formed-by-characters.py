class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0
        for word in words:
            word_count = Counter(word)
            if all(char_count[c] >= cnt for c, cnt in word_count.items()):
                total += len(word)
        return total
