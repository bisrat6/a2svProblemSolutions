class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # if more than 1 zero, shrink
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # update result: window length minus one zero
            res = max(res, right - left)

        return res