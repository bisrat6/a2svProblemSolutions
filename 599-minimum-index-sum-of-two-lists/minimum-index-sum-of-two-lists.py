from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapping = {value: index for index, value in enumerate(list1)}
        
        result = []
        min_sum = float('inf')  
        
        for i, value in enumerate(list2):
            if value in mapping:
                index_sum = i + mapping[value]
                
                if index_sum < min_sum:
                    result = [value]
                    min_sum = index_sum
                elif index_sum == min_sum:
                    result.append(value)
                    
        return result
