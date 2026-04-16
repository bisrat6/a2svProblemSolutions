class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector <int> array;
        double median;
        if (nums1.size()>=nums2.size()){
            int i=0;
            while (i<nums2.size()){
                nums1.push_back(nums2[i]);
            i++;
            }
            array=nums1;
        }
        else if (nums2.size()>nums1.size()){
            int i=0;
            while (i<nums1.size()){
                nums2.push_back(nums1[i]);
            i++;
            }
            array=nums2;
        }
        std::sort(array.begin(),array.end());
    if(array.size()%2==0)median=(array[array.size()/2]+array[array.size()/2 -1])*1.0/2;
    else median=array[array.size()/2];
    return median;
    }
};