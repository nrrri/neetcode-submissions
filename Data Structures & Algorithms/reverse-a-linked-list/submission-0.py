# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None, head
        
        while curr: # is not null (last node)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

"""
0->1->2
head 0, next = 1, [prev = null]
head 1, next = 2, [prev = 0]
head 2, next = null, [prev = 1]

what they want
2->1->0
head 2, next = 1, [prev = null]
head 1, next = 0, [prev = 2]
head 0, next = null, [prev = 1] -> next -> prev head
----
0<-1<-2
set temp prev = null
head 0, next = null, [prev = 1] | keep temp to store next then set new next = prev, prev = curr
head 1, next = 0, [prev = 2]
head 2, next = 1, [prev = null]

how to start
    - create node, prev, next
    - switch prev and next

what to check
    - this in only one pointer (next)
    - if head exist -> switch node
    - if not return
"""