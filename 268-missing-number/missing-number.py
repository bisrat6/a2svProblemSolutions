class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=(len(nums)**2+len(nums))//2
        return total-sum(nums)
        

