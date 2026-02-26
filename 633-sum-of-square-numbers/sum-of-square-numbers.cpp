class Solution {
public:
    bool judgeSquareSum(int c) {
        int i=0;
        int j=pow(c,0.5);
        long long sum;
        while (i<=j){
           sum=(long long)i*i+(long long)j*j;
            if(sum<c)i++;
            else if(sum>c)j--;
            else return true;
        }
        return false;

    }
};