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
