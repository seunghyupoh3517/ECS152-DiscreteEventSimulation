import Packet
# Double Linked List -> consider as node to be used in Global Event List
class Event(object):
    def __init__(self, time, packet, next_event, prev_event, is_arrival):
        self.time = time
        # arrival event = arrival time = current time + inter-arrival time (lambda)
        # departure event = departure time = current time + transmission time (mu)
        self.packet = packet
        self.next = next_event # next event
        self.prev = prev_event # previous event
        self.type = is_arrival # boolean value / True = arrival,  False = departure

    def getEventTime(self):
        return self.time # return arrival or departure time

    def getServiceTime(self):
        return self.packet.service_time # get service time = transmission time

    def getType(self):
        return self.type # boolean value whether it is arrival or departure event
