# Double Linked List sorted in increasing order
# https://www.geeksforgeeks.org/create-doubly-linked-list-using-double-pointer-inserting-nodes-list-remains-ascending-order/
# sorted insert in doubly linked list with head/tail pointer
class Global_Event_List(object):
    #head = None
    #tail = None
    def __init__(self, time, head, tail ):
        self.time = Event.time
        self.head = head
        self.tail = tail

    def insert(self, time, bool):
        event1  = Event(time, None, None, bool)
        # No event yet
        if self.head is None:
            self.head = self.tail = event1
        # the last event
        else:
            event1 = self.tail
            # goes to the end of the GEL

    def remove(self):
        current_event = self.head
        if current_event.next is None:
            self.head = current_event
            # no event left in GEL
        else:
            self.head = current_event.next
            self.head.prev = None
        return current_event