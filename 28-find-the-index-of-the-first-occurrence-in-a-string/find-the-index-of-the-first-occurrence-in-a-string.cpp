class Solution {
    public:
        int strStr(string haystack, string needle) {
            string result="";
            for (int i=0;i<needle.length();i++){
                for (int j=0;j<haystack.length();j++){
                   if(haystack.length()-j<needle.length()){
                    return -1;
                   }
                else if (needle[i]==haystack[j]){
                     result+=haystack.substr(j,needle.length());
                     cout<<result<<endl;
                        if (result==needle){
                            return j;
                        }
    
                    }
                     result="";
                }
            
            }
            return -1;
        }
    };