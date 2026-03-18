class Solution {
    public:
        double myPow(double x, int n) {
            if(n==0 || x==1 || (x==-1 && n%2==0))return 1;
            else if( n == INT_MIN)return 0;
            else if(x==-1 && n%2!=0)return -1;
            double integer=1;
            bool check=true;
            if(n<0){
                n=-1*n;
                check=false;
            }
            for (int i=0;i<n;i++){
                integer*=x;
            }
            if (!check)integer=1/integer;

            return integer;
        }
    };