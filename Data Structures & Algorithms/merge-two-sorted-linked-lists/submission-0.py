# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        # check if list1 and list2
        # compare -> list1 and 2
        # note: next = address
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            # move node to next list
            node = node.next
        
        node.next = list1 or list2 # if one of it's done then link the rest
        return dummy.next # return dummy bc node keeps moving to the last
       
