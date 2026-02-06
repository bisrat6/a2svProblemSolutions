class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_map <int,int> mp;
        vector <int> result;
        for(int i=0;i<nums.size();i++){
            if(mp.find(nums[i])==mp.end())mp.insert({nums[i],0});
            mp[nums[i]]++;
            if(mp[nums[i]]==2)result.push_back(nums[i]);
        }
        return result;
    }
};