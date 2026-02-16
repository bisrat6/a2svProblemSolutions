class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
            if i<10:
                result.append(i)
            else:
                n=str(i)
                for j in n:
                    result.append(int(j))
        return result