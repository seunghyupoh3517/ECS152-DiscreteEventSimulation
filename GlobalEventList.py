import Event
import Packet
# Double Linked List sorted in increasing order
# https://www.geeksforgeeks.org/create-doubly-linked-list-using-double-pointer-inserting-nodes-list-remains-ascending-order/
# sorted insert in doubly linked list with head/tail pointer
class Global_Event_List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # NOTICE: Added another parameter "PACKET"
    def insert(self, time, is_arrival,packet): # insert event
        new_event = Event(time, packet, None, None, is_arrival)

        if self.head is None:
            self.head = self.tail = new_event
            return None

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
                        new_event.prev.next = new_event # refers to current node as long as x.prev not null
                    break

            if curr_event.time < new_event.time:
                new_event.next = curr_event.next
                curr_event.next.prev = new_event # refers to current node as long as x.next not null
                curr_event.next = new_event
                new_event.prev = curr_event

    def remove(self): # remove event
        if self.head is None:
            return None
        else:
            curr_event = self.head
            self.head = curr_event.next
            self.head.prev = None
        return curr_event

    def print(self): # testing if the times are sorted in increasing order
        print("Testing times in GEL")
        curr_event = self.head
        while curr_event is not None:
            print(curr_event.time, curr_event.is_arrival)
            curr_event = curr_event.next
