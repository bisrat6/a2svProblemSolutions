class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix[0].size()-1;
        int left=0;
        int right=matrix.size()-1;
        int index=-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            if(matrix[mid][m]<target)left=mid+1;
            else if(matrix[mid][m]>target){
                index=mid;
                right=mid-1;
            }
            else if (matrix[mid][m]==target)return true;
        }
        if(index==-1)return false;
        left=0;
        right=m;
        while(left<=right){
            int mid=left+(right-left)/2;
            if(matrix[index][mid]==target)return true;
            else if(matrix[index][mid]>target)right=mid-1;
            else left=mid+1;
        }
        return false;
    }
};