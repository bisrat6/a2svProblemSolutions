class Solution:
    def twoCitySchedCost(self, costs):
        # sort by difference
        costs.sort(key=lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        total = 0
        
        # first n → A
        for i in range(n):
            total += costs[i][0]
        
        # last n → B
        for i in range(n, 2*n):
            total += costs[i][1]
        
        return total