# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2

        dummy=sol=ListNode()

        while curr1 and curr2:
            if curr1.val>curr2.val:
                nNode=ListNode(curr2.val)
                curr2=curr2.next
            else:
                nNode=ListNode(curr1.val) 
                curr1=curr1.next
            sol.next=nNode
            sol=sol.next

        #attaching remaining
        while curr1:
            nNode=ListNode(curr1.val) 
            curr1=curr1.next
            sol.next=nNode
            sol=sol.next
        
        while curr2:
            nNode=ListNode(curr2.val) 
            curr2=curr2.next
            sol.next=nNode
            sol=sol.next

        return dummy.next
                


                
