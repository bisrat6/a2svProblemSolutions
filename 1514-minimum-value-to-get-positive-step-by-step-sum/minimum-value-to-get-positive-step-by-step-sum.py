class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val=101
        summ=0
        for i in nums:
            summ+=i
            min_val=min(summ,min_val)
        if min_val>0:
            return 1
        else:
            return min_val*-1+1
