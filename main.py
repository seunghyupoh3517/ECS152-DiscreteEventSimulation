# Discrete Event Simulation
# main file
import queue
import random
import math
from Packet import Packet
import GlobalEventList
import matplotlib.pyplot as plt
import Event

# inter-arrival time: use lambda for rate
# transmission time: use mu for rate
def negative_exponentially_distributed_time(rate):
    # u = drand48()
    u = random.random()
    return ((-1 / rate) * math.log(1 - u))


print("Start")
# Experiment set loading
arrival_rate_list = [0.1, 0.2, 0.4, 0.5, 0.6, 0.80, 0.9]
MAXBUFFER_list = [1, 20, 30]
service_rate = 1

arrival_rate = arrival_rate_list[0]
MAXBUFFER = 99999999
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

# insert first arrival packet into the GEL
arr_time = negative_exponentially_distributed_time(arrival_rate)
pak = Packet(negative_exponentially_distributed_time(service_rate),0)
GEL.insert(time + arr_time, True, pak)


# Statistics
# Utilization: what fraction of time server busy -> keep running count of the times server is busy
# time for server busy / total time
# Mean queue length: sum of the area under the curve / total time
# Number of packets  dropped: keep running  count of packets dropped, when it arrives at the buffer
pak_num = 1
server_busy_time = 0    # server_busy_time / time
prev_time = 0
length_list = []
time_list = []
# server_start = -1       # time - server_start  = server operating time
#                         # check when it changes
area = 0                # area += packet length * time
curr_length = 0         # curr_length = length
prev_length = 0         # packet length in every step -> prev_length = curr_length
dropped_packet = 0

# Simulation starts
for i in range(0, 100000):
    # Set current time to be event time
    # print(i)
    current_event = GEL.remove()
    time = current_event.time
    width = time - prev_time                 # time interval between two events happen
    print(i, time, current_event.type, current_event.packet.num )
    prev_time = time

    # Arrival event process
    if current_event.type:
        # schedule the next arrival event and insert into GEL
        next_packet = Packet(negative_exponentially_distributed_time(service_rate),pak_num)
        pak_num +=1
        GEL.insert(time + negative_exponentially_distributed_time(arrival_rate), True, next_packet)
        # print(negative_exponentially_distributed_time(arrival_rate))

        # Process Arrival Event -> deal with packet / buffer (queue) / GE
        if length == 0:                       # server is free, transmit immediately -> create departure event
            GEL.insert(time + current_event.packet.service_time, False, current_event.packet)
            length += 1

        elif length > 0:
            if MAXBUFFER > length - 1:        # server is busy, add packet to the queue
                buffer.put(current_event.packet)
                length += 1
            else:                             # exceed buffer size, drop packet
                dropped_packet += 1


    # Departure event process
    else:
        # Process Departure Event -> deal with server / GEL
        # set current time = event time
        # update statistics which maintain the mean queue-length and server busy time
        # packet departure -> decrement the length

        server_busy_time += current_event.getServiceTime()     # add the service time which is the busy time of the server when process this departure packet
        length -= 1

        # if queue is empty, length ==0, do nothing
        # if queue is not empty, length >  0
        # 1. dequeue the first packet from the buffer
        # 2. create new departure event  for a time, currenttime +  transmissiontime
        # 3. insert the event in the GEL

        if length == 0:             # queue is empty
            pass
            # do nothing except when the server started
            # if server_start != -1:
            #     server_busy_time += time - server_start
            #     server_start = -1 # reset

        elif length > 0:            # queue is not empty
            departure_packet = buffer.get()       # remove and return an item - remove it from queue
            GEL.insert(time + departure_packet.service_time, False, departure_packet)

    # compute statistics data
    curr_length = length
    area += prev_length * width
    prev_length = curr_length

    length_list.append(curr_length)
    time_list.append(time)
    # # for arrival
    # if server_start != -1:
    #     server_busy_time += time - server_start

# Statistics
print("COLLECTING STATISTICS!")
print("Utilization: ", server_busy_time / time)
print("Mean queue length: ", area / time)
print("Numbers of packets dropped: ", dropped_packet)
print("length of time list", len(time_list))
# list1 = [1,2,1,2,3,4,3,4,5,4]
# list2 = [1,3,2,5,6,4,2,4,9,10]
# plt.step(list2, list1)
plt.step(time_list, length_list)
plt.show()
