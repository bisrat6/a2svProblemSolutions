from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Count frequencies to find the dominant element
        count = Counter(nums)
        dominant, totalCount = max(count.items(), key=lambda x: x[1])
        
        leftCount = 0
        
        for i in range(n - 1):
            if nums[i] == dominant:
                leftCount += 1
            
            # Check if dominant remains dominant in both parts
            if leftCount * 2 > (i + 1) and (totalCount - leftCount) * 2 > (n - i - 1):
                return i
        
        return -1