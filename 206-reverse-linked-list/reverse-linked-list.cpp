/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
    ListNode*moverhead=head;
    ListNode*temp=nullptr;
    ListNode*temp2=nullptr;
    while(moverhead){
        temp2=moverhead->next;
        moverhead->next=temp;
        temp=moverhead;
        moverhead=temp2;
    }
    head=temp;
    return head;
}
};