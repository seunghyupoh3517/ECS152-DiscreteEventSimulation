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




def experiment_tester(arrival_rate_list, buffer_size):
    mean_queue_length_list = []
    utilization_list = []
    drop_list = []

    for arrival_rate in arrival_rate_list:
        # arrival_rate = arrival_rate_list[6]
        MAXBUFFER = buffer_size
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
        # length_list = []
        # time_list = []
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
            # print(i, time, current_event.type, current_event.packet.num )
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


        # Statistics
        print("COLLECTING STATISTICS!")
        print("arrival rate = ", arrival_rate,",  service rate = ", service_rate, ",  Buffer Size = ", MAXBUFFER)
        print("Utilization: ", server_busy_time / time)
        print("Mean queue length: ", area / time)
        print("Numbers of packets dropped: ", dropped_packet)
        print("-------------------------------------------\n")

        utilization_list.append(server_busy_time / time)
        mean_queue_length_list.append(area / time)
        drop_list.append(dropped_packet)

    experiment_results = [utilization_list, mean_queue_length_list, drop_list]
    return experiment_results




# main tester

print("Start")
# Experiment set loading
arrival_rate_list = [0.1, 0.2, 0.4, 0.5, 0.6, 0.80, 0.9]
MAXBUFFER_list = [1, 20, 30]
service_rate = 1


# plot 1 & 2 mean_queue_length & utilization: 7 arrival rates with infinity buffer size
result = experiment_tester(arrival_rate_list, 9999999)
utilization_result = result[0]
mean_queue_result = result[1]


# plot 3, drop packets number: 6 arrival rates with buffer size = 1
result3 = experiment_tester(arrival_rate_list[1:6], MAXBUFFER_list[0])[2]

# plot 4, drop packets number: 6 arrival rates with buffer size = 20
result4 = experiment_tester(arrival_rate_list[1:6], MAXBUFFER_list[1])[2]

# plot 5, drop packets number: 6 arrival rates with buffer size = 30
result5 = experiment_tester(arrival_rate_list[1:6], MAXBUFFER_list[2])[2]


# plot the statistics simulation
fig1  = plt.figure()
plt.plot(arrival_rate_list, mean_queue_result, marker='o')
fig1.suptitle('Arrival Rate V.S. Mean Queue Length', fontsize=20)
plt.xlabel('Arrival Rate', fontsize=18)
plt.ylabel('Mean Queue Length', fontsize=16)
fig1.savefig('mean_queue_length_plot.jpg')

fig2 = plt.figure()
plt.plot(arrival_rate_list, utilization_result, marker='o')
fig2.suptitle('Arrival Rate V.S. Utilization', fontsize=20)
plt.xlabel('Arrival Rate', fontsize=18)
plt.ylabel('Utilization', fontsize=16)
fig2.savefig('Utilization_plot.jpg')

fig3 = plt.figure()
plt.plot(arrival_rate_list[1:6], result3, marker='o')
fig3.suptitle('Arrival Rate V.S. Drop Packets (Buffer = 1)', fontsize=20)
plt.xlabel('Arrival Rate', fontsize=18)
plt.ylabel('Number of dropped packets', fontsize=16)
fig3.savefig('drop_1.jpg')


fig4 = plt.figure()
plt.plot(arrival_rate_list[1:6], result4, marker='o')
fig4.suptitle('Arrival Rate V.S. Drop Packets (Buffer = 20)', fontsize=20)
plt.xlabel('Arrival Rate', fontsize=18)
plt.ylabel('Number of dropped packets', fontsize=16)
fig4.savefig('drop_20.jpg')


fig5 = plt.figure()
plt.plot(arrival_rate_list[1:6], result5, marker='o')
fig5.suptitle('Arrival Rate V.S. Drop Packets (Buffer = 30)', fontsize=20)
plt.xlabel('Arrival Rate', fontsize=18)
plt.ylabel('Number of dropped packets', fontsize=16)
fig5.savefig('drop_30.jpg')

plt.show()
