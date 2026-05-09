# Definition for singly-linked list.
# class ListNode:
#     def __init__(Annotated, self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        
        len=0
        while curr:
            len+=1
            curr=curr.next
        print(len)

        i=0
        
        if head and n==len:
                return head.next
        
        dummy=curr=head
        while curr and curr.next:
            revindex=(len-1)-i
            print(revindex)
            if revindex==n:
                curr.next=curr.next.next
                return head
            curr=curr.next
            i+=1

        
        
        