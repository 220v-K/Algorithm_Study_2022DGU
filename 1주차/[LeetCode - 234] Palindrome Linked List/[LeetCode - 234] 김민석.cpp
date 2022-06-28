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
    string str = "";
    void stringtoval(ListNode* head) {
        if (head == nullptr)
            return;
        str += to_string(head->val);
        stringtoval(head->next);
    }
    bool isPalindrome(ListNode* head) {
        stringtoval(head);
        string temp = str;
        reverse(str.begin(), str.end());
        if (temp == str)
            return true;
        return false;
    }
};