class Solution:
    def numSubarraysWithSum(self, nums, goal):
        prefix_sum = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            prefix_sum += num
            
            if prefix_sum - goal in freq:
                count += freq[prefix_sum - goal]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count