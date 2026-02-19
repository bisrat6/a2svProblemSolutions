class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums=sorted(nums)
        dic={}
        result=[0]*len(nums)
        for i in range(len(sortedNums)-1,-1,-1):
            if (i>0 and sortedNums[i-1]==sortedNums[i]):
                continue
            dic[sortedNums[i]]=i
        for i in range(len(nums)):
            nums[i]=dic[nums[i]]
        return nums