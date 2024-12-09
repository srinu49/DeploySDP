#!/usr/bin/python3

import subprocess
from subprocess import PIPE, STDOUT, Popen
import pickle
#import dill
# java -jar jFuzzyLogic.jar -e roe.fcl  -1 -0.71 1

# "java -jar tika-app-1.24.1.jar -t 42250_EN_Upload.docx"
# process = Popen(['java', '-jar', 'tika-app-1.24.1.jar', '-t', '42250_EN_Upload.docx'], stdout=PIPE, stderr=PIPE)
# print("hidfg")
# k = subprocess.call(['java', '-jar', 'RoeCompute.jar', 'roe.fcl' , '-1','0', '-0.4'])
# print(k)



# *****************************************Working code 14- 18 ***********************************
# --------------------------------------------------------------------------------------------------
# p = Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'], stdout=PIPE , stderr=STDOUT )# as roeCompute:


# for line in p.stdout:
#     print(line)
#    pass
    #print(roeCompute.stdout.read())
#print(p.)
# print("hi")
# jar_command = ['java', '-jar', 'jFuzzyLogic.jar', '-e', 'roe.fcl' , '-1','0', '-0.4']
# output = subprocess.check_output(jar_command, universal_newlines=True)
# access_rate = '0.7'
# required_rate='1'
# processingtime='-0.5'
# with open('output_of_jar.txt','w') as fp :
#     subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', access_rate, required_rate, processingtime],stdout=fp).wait()
# fp.close()
# f = open("output_of_jar.txt")
# k = float(f.readline())
# print(k)
#************************ Redirect output into a File********************
# ------------------------------------------------------------------------------------------------------------

# https://stackoverflow.com/questions/21510360/how-to-get-the-output-from-jar-execution-in-python-codes
def ic_computeRoE(access_rate, required_rate ,processingtime):
    # print(access_rate+processingtime+required_rate)
    with open('/opt/human-detection/ic_output_of_jar.txt','w') as fp :
        # subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'],stdout=fp).wait()
        subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', access_rate, required_rate, processingtime],stdout=fp).wait()
    fp.close()


   
def ic_computeCcs(roundtriptime, available_resources ,processingspeed):
    # print(access_rate+processingtime+required_rate)
    with open('/opt/human-detection/ic_output_of_jar.txt','w') as fp :
        # subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'],stdout=fp).wait()
        subprocess.Popen(['java', '-jar', 'CcsCompute.jar', 'ccs.fcl', roundtriptime, available_resources, processingspeed],stdout=fp).wait()
    fp.close()


def ic_computeQoE(RoE, Ccs):
    # print(access_rate+processingtime+required_rate)
    with open('/opt/human-detection/ic_output_of_jar.txt','w') as fp :
        # subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'],stdout=fp).wait()
        subprocess.Popen(['java', '-jar', 'QoeCompute.jar', 'qoe.fcl', RoE, Ccs],stdout=fp).wait()
    fp.close()

########  Resize image FIS jar funtion call #############

def ri_computeRoE(access_rate, required_rate ,processingtime):
    # print(access_rate+processingtime+required_rate)
    with open('/opt/human-detection/ri_output_of_jar.txt','w') as fp :
        # subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'],stdout=fp).wait()
        subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', access_rate, required_rate, processingtime],stdout=fp).wait()
    fp.close()


   
def ri_computeCcs(roundtriptime, available_resources ,processingspeed):
    # print(access_rate+processingtime+required_rate)
    with open('/opt/human-detection/ri_output_of_jar.txt','w') as fp :
        # subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'],stdout=fp).wait()
        subprocess.Popen(['java', '-jar', 'CcsCompute.jar', 'ccs.fcl', roundtriptime, available_resources, processingspeed],stdout=fp).wait()
    fp.close()


def ri_computeQoE(RoE, Ccs):
    # print(access_rate+processingtime+required_rate)
    with open('/opt/human-detection/ri_output_of_jar.txt','w') as fp :
        # subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'],stdout=fp).wait()
        subprocess.Popen(['java', '-jar', 'QoeCompute.jar', 'qoe.fcl', RoE, Ccs],stdout=fp).wait()
    fp.close()
    
    
    
########  Extract object FIS jar function call #########
    
def exi_computeRoE(access_rate, required_rate ,processingtime):
    # print(access_rate+processingtime+required_rate)
    with open('/opt/human-detection/exi_output_of_jar.txt','w') as fp :
        # subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'],stdout=fp).wait()
        subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', access_rate, required_rate, processingtime],stdout=fp).wait()
    fp.close()


   
def exi_computeCcs(roundtriptime, available_resources ,processingspeed):
    # print(access_rate+processingtime+required_rate)
    with open('/opt/human-detection/exi_output_of_jar.txt','w') as fp :
        # subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'],stdout=fp).wait()
        subprocess.Popen(['java', '-jar', 'CcsCompute.jar', 'ccs.fcl', roundtriptime, available_resources, processingspeed],stdout=fp).wait()
    fp.close()


def exi_computeQoE(RoE, Ccs):
    # print(access_rate+processingtime+required_rate)
    with open('/opt/human-detection/exi_output_of_jar.txt','w') as fp :
        # subprocess.Popen(['java', '-jar', 'RoeCompute.jar', 'roe.fcl', '-1', '-0.71', '1'],stdout=fp).wait()
        subprocess.Popen(['java', '-jar', 'QoeCompute.jar', 'qoe.fcl', RoE, Ccs],stdout=fp).wait()
    fp.close()
