from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) >= 2:
                res.append(path[:])

            used = set()  # 🔥 avoid duplicates at THIS level

            for i in range(start, len(nums)):
                # condition 1: non-decreasing
                if path and nums[i] < path[-1]:
                    continue
                
                # condition 2: avoid duplicates at same level
                if nums[i] in used:
                    continue
                
                used.add(nums[i])

                path.append(nums[i])          # choose
                backtrack(i + 1, path)       # explore
                path.pop()                   # undo

        backtrack(0, [])
        return res