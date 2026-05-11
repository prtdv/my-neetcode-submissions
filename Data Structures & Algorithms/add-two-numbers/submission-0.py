# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        c1=l1
        c2=l2
        dummy=new=ListNode()
        carry=0

        while c1 and c2:
            sum=c1.val+c2.val+carry
            if sum<10:
                carry=0
                new.next=ListNode(sum)
            else:
                carry=1
                new.next=ListNode(sum-10)
            c1=c1.next
            c2=c2.next
            new=new.next

        while c1:
            sum=c1.val+carry
            carry=0
            if sum<10:
                carry=0
                new.next=ListNode(sum)
            else:
                carry=1
                new.next=ListNode(sum-10)
            c1=c1.next
            new=new.next


        while c2:
            sum=c2.val+carry
            carry=0
            if sum<10:
                carry=0
                new.next=ListNode(sum)
            else:
                carry=1
                new.next=ListNode(sum-10)
            c2=c2.next
            new=new.next
        
        if carry!=0:
            new.next=ListNode(carry)
            
        return dummy.next


