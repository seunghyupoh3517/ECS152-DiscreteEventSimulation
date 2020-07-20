# Double Linked List sorted in increasing order
# https://www.geeksforgeeks.org/create-doubly-linked-list-using-double-pointer-inserting-nodes-list-remains-ascending-order/
# sorted insert in doubly linked list with head/tail pointer
class Global_Event_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, event):
        new_event = event

        if self.head is None: # Empty list
            self.head = self.tail = new_event
        else:
            curr_event = self.head
            while curr_event is not None:
                if curr_event.time > new_event.time:
                    new_event.next = curr_event
                    new_event.prev = curr_event.prev
                    curr_event.prev = new_event

                    if curr_event == self.head:
                        self.head = new_event
                    else:
                        new_event.prev.next = new_event

                    break

            # The new event has the latest time so insert it at the end.
            if curr_event == None:
                curr_event == self.tail
                curr_event.next = new_event
                new_event.prev = curr_event
                new_event.next = curr_event.next
                self.tail = new_event

    def pop_head(self):
        if self.head == None: # Empty list
            return None
        else:
            pop_event = self.head
            self.head = self.head.next
            self.head.prev = None
            return pop_event
