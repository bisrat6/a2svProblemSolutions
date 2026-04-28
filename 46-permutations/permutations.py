from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            # base case: one permutation completed
            if start == len(nums):
                res.append(nums[:])  # copy
                return
            
            for i in range(start, len(nums)):
                # choose
                nums[start], nums[i] = nums[i], nums[start]
                
                # explore
                backtrack(start + 1)
                
                # undo (backtrack)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res