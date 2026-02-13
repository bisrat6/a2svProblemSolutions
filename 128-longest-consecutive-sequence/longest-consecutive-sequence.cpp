class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            if(nums.empty())return 0;
            std::sort(nums.begin(), nums.end());//-1,0,0
            int sum=1;
            int max=1;
            for(int i=1;i<nums.size();i++){
                if(nums[i-1]+1==nums[i]){
                    sum++;}
                else if (nums[i-1]!=nums[i]){
                    if(sum>max)max=sum;
                     sum=1;
                    }
                if(i==nums.size()-1 && sum>max)max=sum;
            }
            return max;
        }
    };