class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_volume=0
        while(left<right):
            temp_volume=min(height[left],height[right])*(right-left)
            max_volume=max(temp_volume,max_volume)

            if height[left]>=height[right]:
                right-=1
            else:
                left+=1

        return max_volume