class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '*':
                stack.pop()      # remove closest character on the left
            else:
                stack.append(ch) # keep the character

        return "".join(stack)