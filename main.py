# Discrete Event Simulation
# main file
import queue
import random
import math
import Packet
import Buffer
import Server
import GlobalEventList
import Event

# time variable contained
class Packet:
    def __init__(self, time): #current time
        self.time = time
    def getTime(self):
        return self.time

# Double Linked List sorted in increasing order
# https://www.geeksforgeeks.org/create-doubly-linked-list-using-double-pointer-inserting-nodes-list-remains-ascending-order/
# sorted insert in doubly linked list with head/tail pointer
class Global_Event_List:
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

# Double Linked List -> consider as node to be used in Global Event List
class Event:
    def __init__(self, time, next, prev, bool):
        self.time = time
        #event time != packet.time
        #arrival/departure time changes in GEL
        self.next = next
        self.prev = prev
        self.arrival = bool
        #True = arrival,  False = departure
        #self.departure = departure
    def getEventTime(self):
        return self.time
    def getArrival(self):
        return self.arrival

# Queue = Buffer
# insert at the end, remove the first packet
#class FIFO:
    #def __init__(self,size):
    #    self.size = size
    #def insert(self):

    #def remove(self):

    #def drop(self):

    #https: // www.geeksforgeeks.org / queue - in -python /
# Can it be running from the main(), insert = enqueue, remove = dequeue,
# drop = if Current Buffer capacity + incoming packet size > MAXBUFFER size - Drop++, else continue

# Link Processor
# 1)idle 2)busy
class Server:
    def  __init(self, data):
    # What else should be contained  in the server?
    # any data needs to be recorded or should we just check whether it's transmitting the data or not at the moment
    # What else should be computed here?

# inter-arrival time: use lamda for rate
# transmission time: use mu for rate
def negative_exponentially_distributed_time(rate):
    # u = drand48()
    u = random.random()
    return ((-1 / rate) * math.log(1 - u))

# Initializing
def main():
# 1. Assume mu = 1 packet/second, lamda = 0.1, 0.2, 0.4, 0.5, 0.6, 0.80, 0.90 packets/second when MAXBUFFER = inf

# 2. Mathematically compute the mean queue lengths, server utilization - compare with 1.

# 3. Assume mu = 1 packet/second, lamda = 0.2, 0.4, 0.5, 0.6, 0.8, 0.9 packets/second when MAXBUFFER = 1,20, 30

    que = queue.Queue() # MAXBUFFER size


    #for i in range(0, 100000):
