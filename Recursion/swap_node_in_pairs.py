from node import Node
from linked_list import LinkedList

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if (head.next is None):
        return head
    else:
        new_head = head.next
        head = head.next.next
        new_head.next = head
        head.next = self.swapPairs(new_head.next.next)

def main():
    new_linked_list = LinkedList()
    new_linked_list.insert_at_end(1)
    new_linked_list.insert_at_end(2)
    new_linked_list.insert_at_end(3)
    new_linked_list.insert_at_end(4)
    print("original linkedlist:", new_linked_list)
    swapPairs(new_linked_list)

main()