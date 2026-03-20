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
    void traverse(TreeNode* p, TreeNode* q,bool&s){
        if(p==NULL and q==NULL) return;
        else if(p==nullptr or q==nullptr or p->val!=q->val)s=false;
        if(s==false)return;
        traverse(p->left,q->left,s);
        traverse(p->right,q->right,s);
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        bool s=true;
        traverse(p,q,s);
        return s;
    }
};