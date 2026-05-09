# Definition for singly-linked list.
# class ListNode:
#     def __init__(Annotated, self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        
        length=0
        while curr:
            length+=1
            curr=curr.next

        i=0
        
        if head and n==length:
                return head.next
        
        curr=head
        removeindex=length-n-1
        while curr and curr.next:
            if i==removeindex:
                curr.next=curr.next.next
                return head
            curr=curr.next
            i+=1

        
        
        