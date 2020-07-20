# Double Linked List -> consider as node to be used in Global Event List
class Event(object):
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