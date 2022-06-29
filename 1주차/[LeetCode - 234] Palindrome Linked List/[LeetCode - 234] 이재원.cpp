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
private:
    ListNode* tail = new ListNode();
    ListNode* startTail = tail;
    ListNode* getEnd(ListNode* head){
        ListNode* end = head;
        while(end->next != nullptr){
            end = end->next;
        }
        return end;
    }
    
    void getReverse(ListNode* head){
        ListNode* temp = getEnd(head);
        tail->val = temp->val;
        ListNode* tempHead = head;
        getReverse_(tempHead);
    }
    
    void getReverse_(ListNode* node){
        if(node->next != nullptr){
            ListNode* newNode = new ListNode(node->val);
            node = node->next;
            getReverse_(node);
            startTail->next = newNode;
            startTail = newNode;
        }
    }
    
public:
    bool isPalindrome(ListNode* head) {
        getReverse(head);
        while(head != nullptr){
            if(head->val == tail->val){
                head = head->next;
                tail = tail->next;
            } else {
                return false;
            }
        }
        return true;
    }
};