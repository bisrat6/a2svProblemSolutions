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
    int sum=0;
    void traverse(TreeNode* root,TreeNode* parent,TreeNode* grandpa){
        if(!root)return ;
        if(grandpa and grandpa->val%2==0)sum+=root->val;
        if(parent)grandpa=parent;
        traverse(root->left,root,grandpa);
        traverse(root->right,root,grandpa);
    }
    int sumEvenGrandparent(TreeNode* root) {
        traverse(root,nullptr,nullptr);
        return sum;
    }
};