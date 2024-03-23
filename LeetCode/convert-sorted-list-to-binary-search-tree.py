# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        prev_mid = self.prev_midnode(head)
        mid = prev_mid.next
        root = TreeNode(mid.val,None,None)
        prev_mid.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
    
    def prev_midnode(self, head):
        slow = fast = head
        prev = None
        while(fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev