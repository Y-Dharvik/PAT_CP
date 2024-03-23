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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == NULL || head -> next == NULL || k == 0){
            return head;
        }
        ListNode* temp = head;
        ListNode* tail = head;
        int n = 0;
        while(temp -> next){
            n++;
            temp = temp -> next;
        }
        tail = temp;
        n++;
        k = n - k%n;
        int i = 0;
        temp = head;
        while(i<k-1){
            temp = temp -> next;
            i++;
        }
        tail -> next = head;
        head = temp -> next;
        temp -> next = NULL;
        return head;
    }
};