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


class Packet:
    def __init__(self, service_time): #current time
        self.service_time = service_time


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


# Each event is a node in the Globle Event List.
class Event:
    def __init__(self, arrival_time, is_arrival, packet):
        # If arrival, arrival time = current time + arrival time.
        # If departure, arrival time = current time + service time.
        self.arrival_time = arrival_time
        self.arrival = is_arrival # Boolean value, True = arrival, False = departure.
        self.packet = packet

    def getArrivalTime(self):
        return self.arrival_time

    def getServiceTime(self):
        return self.packet.service_time

    def isArrival(self):
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
