# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Iteratively
        """
        if (head is None or head.next is None):
            return head
        old_head = head
        while (head.next != None):
            new_head = head.next
            tail = new_head.next
            head.next = tail
            new_head.next = old_head
            old_head = new_head
        return new_head

    def reverseList(self, head):
        return self.reverse(None, head)

    def reverse(self, sol, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Recurively
        """
        if (head is None):
            return sol
        else:
            new = head.next
            head.next = sol
            sol = head
            curr = sol
            # print("recursive")
            # while (curr!=None):
            #     print(curr.val)
            #     curr = curr.next
            return self.reverse(sol, new)