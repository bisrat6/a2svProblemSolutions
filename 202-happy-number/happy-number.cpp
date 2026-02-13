class Solution {
    public:
        bool isHappy(int n) {
            string numstr=to_string(n);
            while(numstr.length()>1){
                int result=0;
                for (int i=0;i<numstr.length();i++){
                    result+=(numstr[i]-'0')*(numstr[i]-'0');
                }
                numstr=to_string(result);
            }
            if(numstr=="1" or numstr=="7") return true;
            return false;   
        }
    };