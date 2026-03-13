from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        max_d = deque()
        min_d = deque()
        left = 0
        ans = 0

        for right in range(len(nums)):

            # maintain decreasing max deque
            while max_d and nums[right] > max_d[-1]:
                max_d.pop()
            max_d.append(nums[right])

            # maintain increasing min deque
            while min_d and nums[right] < min_d[-1]:
                min_d.pop()
            min_d.append(nums[right])

            # shrink window if invalid
            while max_d[0] - min_d[0] > limit:
                if nums[left] == max_d[0]:
                    max_d.popleft()
                if nums[left] == min_d[0]:
                    min_d.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans