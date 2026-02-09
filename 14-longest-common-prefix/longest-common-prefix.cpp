#include <iostream>
#include <vector>
using namespace std;

class Solution {
    public:
        string longestCommonPrefix(vector<string>& strs) {
            string lastElement="";
            for(int j=0;j<strs[0].length();j++)  {
                int i=1;
                while (i<strs.size()){
                    if (strs[0][j]!=strs[i][j]){
                        return lastElement;
                    }
                    i++;
                }
                lastElement+=strs[0][j];
            } 
            return lastElement;
         }
 };