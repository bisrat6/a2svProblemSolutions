#include <algorithm>
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        if (nums.size()==1)return nums[0];
        std::sort(nums.begin(), nums.end()); 
       for (int i=1;i<nums.size()-1;i++){
            if (nums[i-1]!=nums[i]){
                return nums[i-1];
            }
            i++;
        }  
        return nums[nums.size()-1]; 
    }
};