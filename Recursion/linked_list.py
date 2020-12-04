from node import Node


class LinkedList:
    def __init__(self):
        self.start_node = None
    
    def traverse_list(self):
        if (self.start_node is not None):
            spot = self.start_node
            while (spot is not None):
                print(spot.value, " ")
                spot = spot.next
        else:
            print("List has no element")
            return

    # def insert_at_start(self, data):
    #     if (self.start_node is None):
    #         self.start_node = Node(data)
    #     else:
    #         new_node = Node(data)
    #         new_node.next = self.start_node
    #         self.start_node = new_node
    # We do not need to check if it empty, since none will be the next
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if (self.start_node is not None):
            spot = self.start_node
            while (spot.next is not None):
                spot = spot.next
            spot.next = new_node
        else:
            self.start_node = new_node

    #inserting item after another item
    def insert_after_item(self, x, data):
        spot = self.start_node
        while (spot is not None):
            if (spot.value == x):
                new_data = Node(data)
                new_data.next = spot.next
                spot.next = new_data
                break
            spot = spot.next
        print("item not in the list")
        # case: 

    def insert_before_item(self, x ,data):
        # prev = self.start_node
        # if (prev is not None):
        #     spot = prev.next
        #     while (spot is not None):
        #         if (spot.value == x):
        #             new_data = Node(data)
        #             new_data.next = spot
        #             prev.next = new_data
        #             break
        #         prev = prev.next
        #         spot = prev.next
        #     print("item not in the list")
        # else:
        #     print("empty list")
        # The above is not correct, since it does not consider the case that
        # The list only contain one item and that item happen to be the target item
        # This need to be considered since we add before the item instead of after it.
        #########################
        prev = self.start_node
        if (self.start_node is None):
            print("empty list")
            return
        # if the first item is x
        if (prev.value == x):
            new_node = Node(data)
            new_node.next = prev
            self.start_node = new_node
        else:
            spot = prev.next
            while (spot is not None):
                if (spot.value == x):
                    new_data = Node(data)
                    new_data.next = spot
                    prev.next = new_data
                    break
                prev = prev.next
                spot = prev.next
            print("item not in the list")
            # Actually we do not need two pointers,
            # we can use prev only, in the while statment, 
            # use prev.next is not None

    # always pay attention to the first case
    def insert_at_index(self, index, data):
        if (index == 0):
            new_data = Node(data)
            new_data.next = self.start_node
            self.start_node = new_data
            return
        spot = self.start_node
        i = 1
        while (spot is not None):
            if (i == index):
                break
            spot = spot.next
            i += 1
        if (spot is None):
            print("Index out of bound")
        else:
            new_data = Node(data)
            new_data.next = spot.next
            spot.next = new_data
        

