#include <iostream>
using namespace std;
class Solution {
    public:
        int romanToInt(string s) {
        int value=0;
        s+="0";
        for (int index=0;index<s.length()-1;index++){
            if (s[index]=='I'&& s[index+1]=='V'){
                value+=4;
                index++;
            }
            else if (s[index]=='I'&& s[index+1]=='X'){
                value+=9;
                index++;
            }
            else if (s[index]=='X'&& s[index+1]=='L'){
                value+=40;
                index++;
            }
           else if (s[index]=='X'&& s[index+1]=='C'){
                value+=90;
                index++;
            }
           else if (s[index]=='C'&& s[index+1]=='D'){
                value+=400;
                index++;
            }
           else if (s[index]=='C'&& s[index+1]=='M'){
                value+=900;
                index++;
            }
            else{
            switch(s[index]){
                case 'M':
                value+=1000;
                break;
                case 'D':
                value+=500;
                break;
                case 'C':
                value+=100;
                break;
                case 'L':
                value+=50;
                break;
                case 'X':
                value+=10;
                break;
                case 'V':
                value+=5;
                break;
                case 'I':
                value+=1;
                break;}}

        }
return value;
        }
    };
// int main (){

//     Solution solution;
//     cout<<solution.romanToInt("LVIII");
// }