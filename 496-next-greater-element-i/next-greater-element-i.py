class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stack=[]
        result=[]
        for num in nums2:
            while (stack and num>stack[-1]):
                dic[stack[-1]]=num
                stack.pop()
            stack.append(num)
        for num in nums1:
            if num in dic:
                result.append(dic[num])
            else:
                result.append(-1)
        return result
            
        

        # 1,3,4,2,5