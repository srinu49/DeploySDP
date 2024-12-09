import os
import time
initial_time = time.time()
import array as arr
import operator
import random
from executejarfrompy import *

# os.system('ssh pi@10.5.0.163  python3 dummy.py >> /home/administrator/Contribution-3/output.txt')
# ending_time = time.time()
# elapsed_time = str(ending_time - initial_time)
# print('The Round Trip Time is {}'.format(elapsed_time))

# 'all_words[3]'

import paramiko


all_words = []
    with open("pi_ipadd.txt", "r") as file:
    # Read each line
    for line in file:
        # Split the line into words
        words = line.strip().split(',')
        # Add the words to the list
        all_words.extend(words)
    file.close()

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

########## First Node ##############################################33#####################

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('all_words[0]', username='all_words[1]', password='all_words[2]')

#stdin, stdout, stderr = client.exec_command('python3 dummy.py')

#stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')
#stdin, stdout, stderr = client.exec_command('python3 image-resize.py')

#for line in stdout:
#    print(line.strip('\n'))

client.close()

ending_time = time.time()
elapsed_time_pi1 = str(ending_time - initial_time)
#print('The Round Trip Time in sec on 10.5.0.209 is 0')

rtt_c_pi1=eval(elapsed_time_pi1)
# print(k)
RTT_array = []
#RTT_array.append(rtt_c_pi1)
RTT_array.append(0)
# print(a)

################## Second node Start ########################################################

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('all_words[3]', username='all_words[4]', password='all_words[5]')

#stdin, stdout, stderr = client.exec_command('python3 image-resize.py')

# #stdin, stdout, stderr = client.exec_command('python3 dummy.py')

# #stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')
# stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')

#for line in stdout:
#    print(line.strip('\n'))

client.close()

ending_time = time.time()
elapsed_time_pi2 = str(ending_time - initial_time)
reslut2 = eval(elapsed_time_pi2) - eval(elapsed_time_pi1)
#print('The Round Trip Time in sec on all_words[3] (pi-2) when running compression code is {} '.format(reslut2))

rtt_c_pi2=eval(elapsed_time_pi2)
RTT_array.append(rtt_c_pi2-rtt_c_pi1)
# print(a)

#Second node ends


########################### Third Node Start###################################################

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('all_words[6]', username='all_words[7]', password='all_words[8]')

#stdin, stdout, stderr = client.exec_command('python3 image-resize.py')

# #stdin, stdout, stderr = client.exec_command('python3 dummy.py')

# #stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')
# stdin, stdout, stderr = client.exec_command('/home/pi/test/round/compression.py')

#for line in stdout:
#    print(line.strip('\n'))

client.close()

ending_time = time.time()
elapsed_time_pi3 = str(ending_time - initial_time)
reslut3 = eval(elapsed_time_pi3) - eval(elapsed_time_pi2)
#print('The Round Trip Time in sec on all_words[6] (pi-2) when running compression code is {} '.format(reslut3))

rtt_c_pi3=eval(elapsed_time_pi3)
RTT_array.append(rtt_c_pi3 - rtt_c_pi2)
print("Round Trip time array")
print(RTT_array)




maximum = max(RTT_array)

minimun = min(RTT_array)
elapsed_time_pi1 = 0
print("Normalized values")

RTT_normalized_value_on_pi1 =normalization(elapsed_time_pi1, float(minimun), float(maximum))

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


c_RTT_pi3= RTT_array[2]

RTT_normalized_value_on_pi3 =normalization(c_RTT_pi3, float(minimun), float(maximum))

print(RTT_normalized_value_on_pi3)
# print(type(RTT_normalized_value_on_pi1))
Nor_Round_Trip_pi3 = str(RTT_normalized_value_on_pi3)

#part-2

############# GET CPU Speed using shell command ####################################################   'lscpu | grep "CPU max MHz" | awk '{print $4}'  

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('all_words[0]', username='all_words[1]', password='all_words[2]')

stdin, stdout, stderr = client.exec_command('python3 getcpuspeed.py')

Processing_speed_array = []
for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Processing_speed_array.append(eval(line.strip('\n')))
# print("Got you")
# print (Processing_speed_array)




########## GET CPU Speed on node-2###############################################################33

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('all_words[3]', username='all_words[4]', password='all_words[5]')

stdin, stdout, stderr = client.exec_command('python3 getcpuspeed.py')


for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Processing_speed_array.append(eval(line.strip('\n')))
    # Available_resources_array.append(eval(line.strip('\n')))

# print (Processing_speed_array)




######### GET CPU Speed on node-3 ##############################################################33

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('all_words[6]', username='all_words[7]', password='all_words[8]')

stdin, stdout, stderr = client.exec_command('python3 getcpuspeed.py')


for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Processing_speed_array.append(eval(line.strip('\n')))
    # Available_resources_array.append(eval(line.strip('\n')))

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


c_ps_pi3 = Processing_speed_array[2]

Processing_speed_normalized_value_on_pi3 =normalization(c_ps_pi3, float(minimun), float(maximum))

# print(Processing_speed_normalized_value_on_pi2)
# print(type(Processing_speed_normalized_value_on_pi2))
Nor_p_s_pi3 = str(Processing_speed_normalized_value_on_pi3)
print(Nor_p_s_pi3)
# print(type(Nor_p_s_pi3))



# print(Available_resources_array)
### Part -3 
############## GET Available Resources on Node-1 ################################3

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('all_words[0]', username='all_words[1]', password='all_words[2]')

stdin, stdout, stderr = client.exec_command('python3 /home/pi/pipeline-2/memory_cpu_percentage.py')

Available_resources_array = []

for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Available_resources_array.append(eval(line.strip('\n')))
# print("Got you")
# print (Available_resources_array)


######### GET Availaable Resources on Node -2 ######################33333

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('all_words[3]', username='all_words[4]', password='all_words[5]')

stdin, stdout, stderr = client.exec_command('python3 memory_cpu_percentage.py')


for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Available_resources_array.append(eval(line.strip('\n')))

# print (Available_resources_array)


######### GET Availaable Resources on Node -3 ######################33333

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('all_words[6]', username='all_words[7]', password='all_words[8]')

stdin, stdout, stderr = client.exec_command('python3 memory_cpu_percentage.py')


for line in stdout:
    # Process each line in the remote output
    # print(line.strip('\n'))
    Available_resources_array.append(eval(line.strip('\n')))

print("Available Resources array")
print (Available_resources_array)



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


c_Ar_pi3 = Available_resources_array[2]

Available_resources_normalized_value_on_pi3 =normalization(c_Ar_pi3, float(minimun), float(maximum))

print(Available_resources_normalized_value_on_pi3)
# print(type(Processing_speed_normalized_value_on_pi1))
Nor_A_r_pi3= str(Available_resources_normalized_value_on_pi3)        # Send this string as a input to the CCS.fcl file
# print(type(Nor_p_s_pi1))




#############################################################################################3333


Resource_availability_normalized_value = '1'

Processing_speed_normalized_value = '1'

# computeRoE(Nor_Round_Trip_pi1, Resource_availability_normalized_value, Processing_speed_normalized_value )

Ccs = []

ri_computeCcs(Nor_Round_Trip_pi1, Nor_A_r_pi1, Nor_p_s_pi1)
f = open("/home/pi/pipeline-2/ri_output_of_jar.txt")
k = float(f.readline())
Ccs.append(k)
print("CCs of Pi-1",k)
# print("RoE", RoE)

ri_computeCcs(Nor_Round_Trip_pi2, Nor_A_r_pi2, Nor_p_s_pi2)
f = open("/home/pi/pipeline-2/ri_output_of_jar.txt")
k = float(f.readline())
Ccs.append(k)
print("Ccs of Pi-2",k)

ri_computeCcs(Nor_Round_Trip_pi3, Nor_A_r_pi3, Nor_p_s_pi3)
f = open("/home/pi/pipeline-2/ri_output_of_jar.txt")
k = float(f.readline())
Ccs.append(k)
print("Ccs of Pi-3",k)

print("CCS values of available fog instances")
print(Ccs)

max_ccs_index, value = max(enumerate(Ccs), key=operator.itemgetter(1))                  # to get the max value index
print(max_ccs_index)


##################################### Computing RoE starts from here #################################################################

max_access_rate = 10   # per sce 
min_access_rate = 1 

max_required_resources = 4   # no cores
min_required_resources = 1

max__processing_time = 4000   # milli seconds
min_processing_time = 700

###########  define your current application expectation values  ####################3333333

expected_access_rate = 4
expected_required_resources = 2
expected_processing_time = 2000

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

ri_computeRoE(Nor_image_compression_accessrate, Nor_image_compression_requiredresources, Nor_image_compression_processingtime)
f = open("/home/pi/pipeline-2/ri_output_of_jar.txt")
k = float(f.readline())
RoE.append(k)
print("RoE of Image compression", k)

print(RoE)


################3  Computing QoE starts from here #######################################################33
QoE = []

for i in RoE:
    for j in Ccs:
        ri_computeQoE(str(i), str(j))
        f = open("/home/pi/pipeline-2/ri_output_of_jar.txt")
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
print("Selected Node for performing image resize operation::::", random_max_index)
#print(type(max_QoE_index))
#print("Found a suitable node for the task Image Resize")
print("###############QoE Algorithem Ends####################") 
#   Send a token on the selected node to perform an action one python  script is running all the time to read a data from the Compression_token.txt

if(random_max_index == 0):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('all_words[0]', username='all_words[1]', password='all_words[2]')
    sftp = client.open_sftp()
    try:
        f = sftp.open("/home/pi/pipeline-2/Compression_token.txt", 'w')
    except IOError:
        pass
    f.write("resize")
    f.close()
    client.close()


if(random_max_index == 1):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('all_words[3]', username='all_words[4]', password='all_words[5]')
    sftp = client.open_sftp()
    try:
        f = sftp.open("/home/pi/Resize_token.txt", 'w')
    except IOError:
        pass
    f.write("resize")
    f.close()
    client.close()


if(random_max_index == 2):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('all_words[6]', username='all_words[7]', password='all_words[8]')
    sftp = client.open_sftp()
    try:
        f = sftp.open("/home/all_words[7]/Resize_token.txt", 'w')
    except IOError:
        pass
    f.write("resize")   
    f.close()
    client.close()



# https://www.tutorialspoint.com/python-program-to-calculate-the-round-trip-time-rtt
# https://stackoverflow.com/questions/28411960/execute-a-command-on-remote-machine-in-python
