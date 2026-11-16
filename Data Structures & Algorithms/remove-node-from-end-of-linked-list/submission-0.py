# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next

        # summary
        # start from the back l,r -> r = last, l = last - n
        # if start from front = l -> r have an n offset
        # add dummy at first so the last still count
        # ex. [1,2,3,4] n = 2
        #      x   x
        #        x   x
        #          l   r
        #              ^ out of bound -> remove 3, but we're at this node, so we need to add dummy so we can remove the next node 

