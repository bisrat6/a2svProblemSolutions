from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for left, right in zip(l, r):
            sub = nums[left:right+1]
            sub.sort()
            # check if consecutive differences are equal
            diff = sub[1] - sub[0]
            ok = True
            for i in range(2, len(sub)):
                if sub[i] - sub[i-1] != diff:
                    ok = False
                    break
            res.append(ok)
        return res
