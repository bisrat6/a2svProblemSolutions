class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int,int> mp;
        vector<int> result;
        for(int i=0;i<nums.size();i++){
            if(mp.find(nums[i])==mp.end())mp.insert({nums[i],0});
            mp[nums[i]]++;
        }
         for (const auto& pair : mp) {
            if(pair.second>nums.size()/3)result.push_back(pair.first);
         }
         return result;
    }
};