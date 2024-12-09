import os
import time
initial_time = time.time()
import array as arr
import random
import operator
from executejarfrompy import *
import paho.mqtt.client as paho
from sendcmsd import *

# os.system('ssh pi@10.5.0.163  python3 dummy.py >> /home/administrator/Contribution-3/output.txt')
# ending_time = time.time()
# elapsed_time = str(ending_time - initial_time)
# print('The Round Trip Time is {}'.format(elapsed_time))

# '10.5.1.32'

import paramiko


def normalization(current, mini, maxi):
    # print("enter min, max")
    min_m = float(mini)
    max_m = float(maxi)
    # print("current")

    current = current
    numarator = 2*current-min_m-max_m
    demominator= max_m-min_m
    normalization = numarator / demominator
    return normalization

########## First Node  GPU ##############################################33#####################

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.2.12.118', username='srinivas', password='srinu49cmsd')

#stdin, stdout, stderr = client.exec_command('python3 dummy.py')

#stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')
#stdin, stdout, stderr = client.exec_command('python3 /home/administrator/srinivas/experiment2-debian/python3-flask/extractobjects2.py')

#for line in stdout:
#    print(line.strip('\n'))

client.close()

ending_time = time.time()
elapsed_time_pi1 = str(ending_time - initial_time)
print('The Round Trip Time in sec on 10.2.12.118 (pi-1) cmsd when running  {} '.format(elapsed_time_pi1))

rtt_c_pi1=eval(elapsed_time_pi1)
# print(k)
RTT_array = []
RTT_array.append(rtt_c_pi1)
# print(a)

################## Second node Start ########################################################

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.5.1.153', username='angel', password='angel171')

#stdin, stdout, stderr = client.exec_command('python3 /home/charan/srinivas/extractobjects2.py')

# #stdin, stdout, stderr = client.exec_command('python3 dummy.py')

# #stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')
# stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')

#for line in stdout:
#    print(line.strip('\n'))

client.close()

ending_time = time.time()
elapsed_time_pi2 = str(ending_time - initial_time)
reslut2 = eval(elapsed_time_pi2) - eval(elapsed_time_pi1)
print('The Round Trip Time in sec on 10.5.1.32 (pi-2) angel when running compression code is {} '.format(reslut2))

rtt_c_pi2=eval(elapsed_time_pi2)
RTT_array.append(rtt_c_pi2-rtt_c_pi1)
# print(a)

#Second node ends


########################### Third Node Start###################################################

# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect('10.5.1.40', username='pi-cv-101', password='cv101')

# stdin, stdout, stderr = client.exec_command('python3 compressimage.py')

# # #stdin, stdout, stderr = client.exec_command('python3 dummy.py')

# # #stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')
# # stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')

# for line in stdout:
#     print(line.strip('\n'))

# client.close()

# ending_time = time.time()
# elapsed_time_pi3 = str(ending_time - initial_time)
# reslut3 = eval(elapsed_time_pi3) - eval(elapsed_time_pi2)
# print('The Round Trip Time in sec on 10.5.1.40 (pi-2) when running compression code is {} '.format(reslut3))

# rtt_c_pi3=eval(elapsed_time_pi3)
# RTT_array.append(rtt_c_pi3 - rtt_c_pi2)
# print("Round Trip time array")
# print(RTT_array)

# print(rtt_c_pi3)
# print("pi2 {}" .format(rtt_c_pi2))
# Third Node Ends
# ADD value into an array and then find min and max from that array

# Fourth Node starts

# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect('10.5.1.52', username='pi', password='lockthis')

# stdin, stdout, stderr = client.exec_command('python3 compressimage.py')

# # #stdin, stdout, stderr = client.exec_command('python3 dummy.py')

# # #stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')
# # stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')

# for line in stdout:
#     print(line.strip('\n'))

# client.close()

# ending_time = time.time()
# elapsed_time_pi3 = str(ending_time - initial_time)
# reslut = eval(elapsed_time_pi3) - eval(elapsed_time_pi2)
# print('The Round Trip Time in sec on 10.5.1.32 (pi-2) when running compression code is {} '.format(reslut))

# rtt_c_pi3=eval(elapsed_time_pi3)
# a.append(rtt_c_pi3 - rtt_c_pi2)
# print(a)

# Fourth Node Ends




# b=10
# a.append(b)
# print(a)

# rang = arr.array('f', eval(elapsed_time))

# print(rang)

maximum = max(RTT_array)

minimun = min(RTT_array)

print("Normalized values")

RTT_normalized_value_on_pi1 =normalization(eval(elapsed_time_pi1), float(minimun), float(maximum))

print(RTT_normalized_value_on_pi1)
# print(type(RTT_normalized_value_on_pi1))
Nor_Round_Trip_pi1 = str(RTT_normalized_value_on_pi1)
# print(type(Nor_Round_Trip_pi1))




c_RTT_pi2= RTT_array[1]

RTT_normalized_value_on_pi2 =normalization(c_RTT_pi2, float(minimun), float(maximum))

print(RTT_normalized_value_on_pi2)
# print(type(RTT_normalized_value_on_pi1))
Nor_Round_Trip_pi2 = str(RTT_normalized_value_on_pi2)
# print(type(Round_Trip_pi1))


# c_RTT_pi3= RTT_array[2]

# RTT_normalized_value_on_pi3 =normalization(c_RTT_pi3, float(minimun), float(maximum))

# print(RTT_normalized_value_on_pi3)
# # print(type(RTT_normalized_value_on_pi1))
# Nor_Round_Trip_pi3 = str(RTT_normalized_value_on_pi3)

#part-2

############# Node-1 GET CPU Speed using shell command ####################################################   'lscpu | grep "CPU max MHz" | awk '{print $4}'  

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.2.12.118', username='srinivas', password='srinu49cmsd')

stdin, stdout, stderr = client.exec_command('python3 /home/srinivas/Contribution-3/Automate_pipeline/getcpuspeed.py')

Processing_speed_array = []
for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Processing_speed_array.append(eval(line.strip('\n')))
print("Got you")
print (Processing_speed_array)




########## GET CPU Speed on node-2  charan ###############################################################33

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.5.1.153', username='angel', password='angel171')

stdin, stdout, stderr = client.exec_command('python3 /home/angel/srinivas/getcpuspeed.py')


for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Processing_speed_array.append(eval(line.strip('\n')))
    # Available_resources_array.append(eval(line.strip('\n')))

# print (Processing_speed_array)



print("Processing Speed Array")
print(Processing_speed_array)



maximum = max(Processing_speed_array)

minimun = min(Processing_speed_array)

if(minimun == maximum):
    minimun=0

c_ps_pi1 = Processing_speed_array[0]

Processing_speed_normalized_value_on_pi1 =normalization(c_ps_pi1, float(minimun), float(maximum))

print("Processing speed normalized values")

print(Processing_speed_normalized_value_on_pi1)
# print(type(Processing_speed_normalized_value_on_pi1))
Nor_p_s_pi1 = str(Processing_speed_normalized_value_on_pi1)        # Send this string as a input to the CCS.fcl file
# print(type(Nor_p_s_pi1))


c_ps_pi2 = Processing_speed_array[1]

Processing_speed_normalized_value_on_pi2 =normalization(c_ps_pi2, float(minimun), float(maximum))

# print(Processing_speed_normalized_value_on_pi2)
# print(type(Processing_speed_normalized_value_on_pi2))
Nor_p_s_pi2 = str(Processing_speed_normalized_value_on_pi2)
print(Nor_p_s_pi2)
# print(type(Nor_p_s_pi2))


# c_ps_pi3 = Processing_speed_array[2]

# Processing_speed_normalized_value_on_pi3 =normalization(c_ps_pi3, float(minimun), float(maximum))

# # print(Processing_speed_normalized_value_on_pi2)
# # print(type(Processing_speed_normalized_value_on_pi2))
# Nor_p_s_pi3 = str(Processing_speed_normalized_value_on_pi3)
# print(Nor_p_s_pi3)
# print(type(Nor_p_s_pi3))



# print(Available_resources_array)
### Part -3 
############## GET Available Resources on Node-1 ################################3

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.2.12.118', username='srinivas', password='srinu49cmsd')

stdin, stdout, stderr = client.exec_command('python3 /home/srinivas/Contribution-3/Automate_pipeline/memory_cpu_percentage.py')

Available_resources_array = []

for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Available_resources_array.append(eval(line.strip('\n')))
# print("Got you")
# print (Available_resources_array)


######### GET Availaable Resources on Node -2  charan ######################33333

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.5.1.153', username='angel', password='angel171')

stdin, stdout, stderr = client.exec_command('python3 /home/angel/srinivas/memory_cpu_percentage.py')


for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Available_resources_array.append(eval(line.strip('\n')))

# print (Available_resources_array)


######### GET Availaable Resources on Node -3 ######################33333

# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect('10.5.1.40', username='pi-cv-101', password='cv101')

# stdin, stdout, stderr = client.exec_command('python3 getavailableresources.py')


# for line in stdout:
#     # Process each line in the remote output
#     # print(line.strip('\n'))
#     Available_resources_array.append(eval(line.strip('\n')))

# print("Available Resources array")
# print (Available_resources_array)



maximum = max(Available_resources_array)

minimun = min(Available_resources_array)

if(minimun == maximum):
    minimun=0

c_Ar_pi1 = Available_resources_array[0]

Available_resources_normalized_value_on_pi1 =normalization(c_Ar_pi1, float(minimun), float(maximum))

print("Normalized available resouces values")
print(Available_resources_normalized_value_on_pi1)
# print(type(Processing_speed_normalized_value_on_pi1))
Nor_A_r_pi1 = str(Available_resources_normalized_value_on_pi1)        # Send this string as a input to the CCS.fcl file
# print(type(Nor_p_s_pi1))


c_Ar_pi2 = Available_resources_array[1]

Available_resources_normalized_value_on_pi2 =normalization(c_Ar_pi2, float(minimun), float(maximum))

print(Available_resources_normalized_value_on_pi2)
# print(type(Processing_speed_normalized_value_on_pi1))
Nor_A_r_pi2= str(Available_resources_normalized_value_on_pi2)        # Send this string as a input to the CCS.fcl file
# print(type(Nor_p_s_pi1))
# print(type(Nor_p_s_pi2))


# c_Ar_pi3 = Available_resources_array[2]

# Available_resources_normalized_value_on_pi3 =normalization(c_Ar_pi3, float(minimun), float(maximum))

# print(Available_resources_normalized_value_on_pi3)
# # print(type(Processing_speed_normalized_value_on_pi1))
# Nor_A_r_pi3= str(Available_resources_normalized_value_on_pi3)        # Send this string as a input to the CCS.fcl file
# print(type(Nor_p_s_pi1))




#############################################################################################3333


Resource_availability_normalized_value = '1'

Processing_speed_normalized_value = '1'

# computeRoE(Nor_Round_Trip_pi1, Resource_availability_normalized_value, Processing_speed_normalized_value )

Ccs = []
exi_computeCcs(Nor_Round_Trip_pi1, Nor_A_r_pi1, Nor_p_s_pi1)
f = open("exi_output_of_jar.txt")
k = float(f.readline())
Ccs.append(k)
print("CCs of Pi-1",k)
# print("RoE", RoE)

exi_computeCcs(Nor_Round_Trip_pi2, Nor_A_r_pi2, Nor_p_s_pi2)
f = open("exi_output_of_jar.txt")
k = float(f.readline())
Ccs.append(k)
print("Ccs of Pi-2",k)

# computeCcs(Nor_Round_Trip_pi3, Nor_A_r_pi3, Nor_p_s_pi3)
# f = open("output_of_jar.txt")
# k = float(f.readline())
# Ccs.append(k)
# print("Ccs of Pi-3",k)

print("CCS values of available fog instances")
print(Ccs)

max_ccs_index, value = max(enumerate(Ccs), key=operator.itemgetter(1))                  # to get the max value index
print(max_ccs_index)


##################################### Computing RoE starts from here #################################################################

max_access_rate = 10   # per sce 
min_access_rate = 1 

max_required_resources = 12   # no cores
min_required_resources = 1

max__processing_time = 10000   # milli seconds
min_processing_time = 700

###########  define your current application expectation values  ####################3333333

expected_access_rate = 4
expected_required_resources = 2
expected_processing_time = 5000

Nor_Access_rate= normalization(expected_access_rate, float(min_access_rate), float(max_access_rate))
print("Access rate Normalized value:", Nor_Access_rate)


Nor_Required_resources= normalization(expected_required_resources, float(min_required_resources), float(max_required_resources))
print("Normalized Required resouce value:", Nor_Required_resources)


Nor_Processsing_time = normalization(expected_processing_time, float(min_processing_time), float(max__processing_time))
print("Normalized processing time value:", Nor_Processsing_time)

###########3 convert Normalized avlues into string and pass it to ccf file ############################

Nor_image_compression_accessrate= str(Nor_Access_rate)
Nor_image_compression_requiredresources= str(Nor_Required_resources)
Nor_image_compression_processingtime= str(Nor_Processsing_time)

RoE = []

exi_computeRoE(Nor_image_compression_accessrate, Nor_image_compression_requiredresources, Nor_image_compression_processingtime)
f = open("exi_output_of_jar.txt")
k = float(f.readline())
RoE.append(k)
print("RoE of Image compression", k)

print(RoE)


################3  Computing QoE starts from here #######################################################33
QoE = []

for i in RoE:
    for j in Ccs:
        exi_computeQoE(str(i), str(j))
        f = open("exi_output_of_jar.txt")
        k = float(f.readline())
        QoE.append(k)
print("QoE Matrix:")
print(QoE)


# Apply Hungarian Maximization Algorithm on QoE matrix; its a one dimentional so it will selects max index all the time in this case..

#max_QoE_index, value = max(enumerate(QoE), key=operator.itemgetter(1))                  # to get the max value index

max_value = max(QoE)                               # new random max index retrive (next 4 lines)
max_indices = [i for i, value in enumerate(QoE) if value == max_value]
if max_indices:
    random_max_index =random.choice(max_indices)
print("selected node for object extraction:::", random_max_index)

#print(max_QoE_index)
#print(type(max_QoE_index))

#   Send a token on the selected node to perform an action one python  script is running all the time to read a data from the Compression_token.txt




if(random_max_index == 0):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.2.12.118', username='srinivas', password='srinu49cmsd')
    sftp = client.open_sftp()
    try:
        f = sftp.open("/home/srinivas/Contribution-3/connect-to-mqtt/Compression_token.txt", 'w')
    except IOError:
        pass
    f.write("extract")
    f.close()
    client.close()
    
    #mqttBroker = "10.5.0.215"
    #port = 1883
    #c=paho.Client("")
    #c.connect(mqttBroker, port)

    #print("listening")

    #c.on_message = on_message
    #c.on_subscribe = on_subscribe

    #c.subscribe("/testmqtt/compress",2) 

    #c.loop_start() 

    #time.sleep(2)

    #c.loop_stop()

    send_remotecmsd()

if(random_max_index == 1):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.5.1.153', username='angel', password='angel171')
    sftp = client.open_sftp()
    try:
        f = sftp.open("/home/angel/srinivas/Compression_token.txt", 'w')
    except IOError:
        pass
    f.write("extract")
    f.close()
    client.close()
    
    #mqttBroker = "10.5.0.215"
    #port = 1883
    #c=paho.Client("")
    #c.connect(mqttBroker, port)

    #print("listening")

    #c.on_message = on_message2
    #c.on_subscribe = on_subscribe

    #c.subscribe("/testmqtt/compress",2) 

    #c.loop_start() 

    #time.sleep(2)

    #c.loop_stop()


# if(max_QoE_index == 2):
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect('10.5.1.40', username='pi-cv-101', password='cv101')
#     sftp = client.open_sftp()
#     try:
#         f = sftp.open("/home/pi-cv-101/Compression_token.txt", 'w')
#     except IOError:
#         pass
#     f.write("compress")   
#     f.close()
#     client.close()



# https://www.tutorialspoint.com/python-program-to-calculate-the-round-trip-time-rtt
# https://stackoverflow.com/questions/28411960/execute-a-command-on-remote-machine-in-python
