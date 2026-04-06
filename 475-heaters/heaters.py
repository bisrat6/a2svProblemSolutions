from bisect import bisect_left
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        radius = 0
        
        for house in houses:
            idx = bisect_left(heaters, house)
            
            left_dist = float('inf')
            right_dist = float('inf')
            
            # distance to left heater
            if idx > 0:
                left_dist = house - heaters[idx - 1]
            
            # distance to right heater
            if idx < len(heaters):
                right_dist = heaters[idx] - house
            
            # closest heater distance
            closest = min(left_dist, right_dist)
            
            # update maximum radius needed
            radius = max(radius, closest)
        
        return radius