class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range (0,len(nums)):
            val=target-nums[i]
            if val in dic:
                return [i,dic[val]]
            dic[nums[i]]=i
        return []

