from Event import Event
import Packet
# Double Linked List sorted in increasing order
# https://www.geeksforgeeks.org/create-doubly-linked-list-using-double-pointer-inserting-nodes-list-remains-ascending-order/
# sorted insert in doubly linked list with head/tail pointer
class Global_Event_List(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_event = 0
    # NOTICE: Added another parameter "PACKET"
    def insert(self, time, is_arrival, packet): # insert event
        new_event = Event(time, packet, None, None, is_arrival)

        if self.head is None:
            self.head = self.tail = new_event
            return None
        else:
            curr_event = self.head
            while curr_event is not None:
                if curr_event.time > new_event.time:
                    if curr_event == self.head:          # add to the front
                        self.head = new_event
                        new_event.next = curr_event
                        curr_event.prev = new_event
                    else:                                # insert in the middle
                        new_event.next = curr_event
                        new_event.prev = curr_event.prev
                        curr_event.prev.next = new_event
                        curr_event.prev = new_event
                    return
                curr_event = curr_event.next


                # add to the end of list
                new_event.next = None
                new_event.prev = self.tail
                self.tail.next = new_event
                self.tail = new_event

        self.num_event += 1


    def remove(self): # remove event
        if self.head is None:
            return None
        else:
            curr_event = self.head
            self.head = curr_event.next
            # self.head.prev = None
        return curr_event

    def print(self): # testing if the times are sorted in increasing order
        print("Testing times in GEL")
        curr_event = self.head
        while curr_event is not None:
            print(curr_event.time, curr_event.is_arrival)
            curr_event = curr_event.next
