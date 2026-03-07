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
    ListNode* oddEvenList(ListNode* head) {
         if (!head || !head->next) return head; 
        ListNode* temp=head;
        ListNode* temp2=head->next;
        ListNode* temp3=temp2;
        while(temp2!=nullptr and temp2->next!=nullptr){
            temp->next=temp->next->next;
            temp2->next=temp2->next->next;
            temp=temp->next;
            temp2=temp2->next;

        }
        temp->next=temp3;
        return head;
    }
};