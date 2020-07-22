# Discrete Event Simulation
# main file
import queue
import random
import math
import Packet
import GlobalEventList
import Event

# inter-arrival time: use lambda for rate
# transmission time: use mu for rate
def negative_exponentially_distributed_time(rate):
    # u = drand48()
    u = random.random()
    return ((-1 / rate) * math.log(1 - u))

def main():
    # 1. Assume mu = 1 packet/second, lambda = 0.1, 0.2, 0.4, 0.5, 0.6, 0.80, 0.90 packets/second when MAXBUFFER = inf
    # 2. Mathematically compute the mean queue lengths, server utilization - compare with 1.
    # 3. Assume mu = 1 packet/second, lambda = 0.2, 0.4, 0.5, 0.6, 0.8, 0.9 packets/second when MAXBUFFER = 1,20,30
    service_rate = float(input("Please enter the arrival rate, μ: ")) # mu = 1 packet/seconds
    arrival_rate = float(input("Please enter the service rate, λ ")) # lambda = 0.1, 0.2, 0.4, 0.5, 0.6, 0.80, 0.90
                                                                     # lambda = 0.2, 0.4, 0.5, 0.6, 0.8, 0.9
    MAXBUFFER = float(input("Please enter the size of MAXBUFFER(type -1 for infinity): ")) # float('inf') or 1, 20, 30

    # Initializing
    # number of packets in the queue, by default 0
    # current time, by default 0
    # set service rate / arrival rate of the packets
    # Create the first arrival event and then insert it into the GEL
    # The event time of the first arrival event is obtained by adding inter-arrival to the current time
    length = 0
    time = 0
    buffer = queue.Queue(MAXBUFFER)
    GEL = GlobalEventList.Global_Event_List()
    GEL.insert(time + negative_exponentially_distributed_time(arrival_rate), True)

    # Statistics
    # Utilization: what fraction of time server busy -> keep running count of the times server is busy
    # time for server busy / total time
    # Mean queue length: sum of the area under the curve / total time
    # Number of packets  dropped: keep running  count of packets dropped, when it arrives at the buffer
    server_busy_time = 0 # server_busy_time / time
    server_start = -1 # time - server_start  = server operating time
                      # check when it changes
    area = 0 # area += packet length * time
    width = 0
    prev_time = 0
    curr_length = 0 # curr_length = length
    prev_length = 0 # packet length in every step -> prev_length = curr_length
    dropped_packet = 0

    # Clock starts
    for i in range(0, 100000):
        # Set current time to be event time
        current_event = GEL.remove()
        time = current_event.time()
        width = time - prev_time
        prev_time = time

        if current_event.is_arrival == True:
            # generate one arrival at a time -> schedule the next arrival
            new_packet = Packet(negative_exponentially_distributed_time(arrival_rate))
            GEL.insert(time + negative_exponentially_distributed_time(service_rate),True)
            # Process Arrival Event -> deal with packet / buffer (queue) / GE
            if length == 0 and MAXBUFFER > 0: # server is free


            elif length > 0 and MAXBUFFER > 0: # server is busy
                if length - 1  < MAXBUFFER:
                    buffer.put(new_packet)
                    length+=1
                elif length - 1 >= MAXBUFFER:
                    dropped_packet+=1

            elif MAXBUFFER == -1: # infinite buffer size


            # Find the time of next arrival, current time, and then + randomly generated time with lamda = inter-arrival
            # Create a new packet and determine its service time = transmission time = randomly generated with mu
            # Create new arrival event
            # insert the event into the GEL, make sure it to be ordered in time, later event at later node
            # a) server is free, length == 0
            # packet immediately transmission, deaprture time = current time + transmission time
            # 1. get the service time
            # 2. create departure event at time = current + transmission time
            # 3. insert the event into GEL (sorted order)
            # b) server is busy, length > 0
            # -> if the  queue is not full, length - 1 < MAXBUFFER
            # put packet into  the queue
            # -> if the queue is full
            # drop the packet and record dropped packet
            # since new arrival event, increment the length
            # update statistics which maintain the mean queue-length and server busy time

        elif current_event.is_arrival  == False:
            # Process Departure Event -> deal with server / GEL
            # set current time = event time
            # update statistics which maintain the mean queue-length and server busy time
            # packet departure -> decrement the length
            transmission_time = current_event.getServiceTime()
            length-=1

            # if queue is empty, length ==0, do nothing
            # if queue is not empty, length >  0
            # 1. dequeue the first packet from the buffer
            # 2. create new departure event  for a time, currenttime +  transmissiontime
            # 3. insert the event in the GEL

            if length == 0: # queue is empty
                # do nothing except when the server started
                if server_start != -1:
                    server_busy_time += time - server_start
                    server_start = -1 # reset

            elif length > 0: # queue is not empty
                departure_event = buffer.get() # remove and return an item - remove it from queue
                GEL.insert(time + departure_event.getServiceTime(),False)

        curr_length = length
        area += prev_length * width
        prev_length = curr_length

        # for arrival
        if server_start != -1:
            server_busy_time += time - server_start

    # Statistics
    print("COLLECTING STATISTICS!")
    print("Utilization: ", server_busy_time / time)
    print("Mean queue length: ", area / time)
    print("Numbers of packets dropped: ", dropped_packet)