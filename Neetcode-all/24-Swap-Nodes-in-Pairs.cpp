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
    ListNode* swapPairs(ListNode* head) {
        if(!head) return nullptr;
        if(!head->next) return head;
        ListNode* cur = head;
        ListNode* main = nullptr;
        ListNode* prev = nullptr;
        while(cur && cur->next){
            ListNode* first = cur->next;
            cur->next = cur->next->next;
            first->next = cur;
            if (prev) prev->next = first;
            if (cur == head) main = first;
            prev = cur;
            cur = cur->next;
            if (cur == nullptr) break;
        }
        return main;
    }
};