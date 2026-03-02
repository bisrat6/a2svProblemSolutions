class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        res = 0

        for right in range(len(s)):
            c = s[right]
            count[c] = count.get(c, 0) + 1
            # update most frequent count in window
            max_freq = max(max_freq, count[c])

            # if replacements needed > k, shrink window
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # update result
            res = max(res, right - left + 1)

        return res