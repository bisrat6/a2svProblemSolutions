class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxCon=0
        tempCount=0
        j=0
        for i in range(len(nums)):
            if nums[i]!=1 and k<=0:
                while k<=0:
                    if nums[j]==0:
                        k+=1
                    j+=1
                    tempCount-=1
            if k>0 and nums[i]==0:
                k-=1
            tempCount+=1
            maxCon=max(tempCount,maxCon)
        return maxCon
