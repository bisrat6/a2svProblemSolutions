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
    ListNode* sortList(ListNode* head) {
        if (head==NULL or head->next==NULL)return head;
        vector<int> array;
        while (head){
            array.push_back(head->val);
            head=head->next;
        }
        std::sort(array.begin(),array.end());
        ListNode* head1=new ListNode(array[0]);
        ListNode* moverhead=head1;
        for(int i=1;i<array.size();i++){
            ListNode* temp=new ListNode(array[i]);
            moverhead->next=temp;
            moverhead=temp;
        }
        moverhead->next=nullptr;
        return head1;
    }
};