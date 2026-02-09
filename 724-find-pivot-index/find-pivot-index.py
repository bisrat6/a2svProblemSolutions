class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr=[]
        arr2=[]
        for i in range(len(nums)):
            if not arr:
                arr.append(nums[len(nums)-i-1])
                arr2.append(nums[i])
            else:
                arr.append(arr[-1]+nums[len(nums)-i-1])
                arr2.append(arr2[-1]+nums[i])
        arr=arr[::-1]
        for i in range(len(nums)):
            if arr[i]==arr2[i]:
                return i
        return -1

            
