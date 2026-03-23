/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void sum(TreeNode* root,vector<int> & store){
        if(!root) return ;
        sum(root->left,store);
        store.push_back(root->val);
        sum(root->right,store);
    }
    bool findTarget(TreeNode* root, int k) {
        vector<int> store;
        sum(root,store);
        int j=store.size()-1;
        int i=0;
        while(i<j){
            if(store[i]+store[j]>k)j--;
            else if(store[i]+store[j]<k)i++;
            else return true;
        }
        return false;
    }
};