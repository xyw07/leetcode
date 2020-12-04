from linked_list import LinkedList


def test_traverse_list():
    new_linked_list = LinkedList()
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(15)
    new_linked_list.insert_at_start(20)
    new_linked_list.insert_after_item(10, 17)
    new_linked_list.insert_before_item(17, 25)
    new_linked_list.insert_at_index(2,8)
    new_linked_list.traverse_list()

test_traverse_list()