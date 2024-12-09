import time
import subprocess

def read_file_forever(file_path):
    while True:
        try:
           
            l = "compress"
            r = "resize"
            with open(file_path, 'r') as file:
                # Read the file contents here
                content = file.read()
                c = content.strip("\n")
                f = open(file_path, 'w')
                # f.write("Done") 
                if c == l:
                    print(c)
                    #print("Got you")
                    

                    # time.sleep(2)
                    # set path of a file compression code here
                    print("On Pi-1 compression token received:: going to call compression task") 
                    command = ["python3", "/home/pi-cv-101/pipeline-2/compress_filereceiver.py"]
                    subprocess.Popen(command)

                    command2 = ["python3", "/home/pi-cv-101/pipeline-2/resize_image_QoE.py"]
                    subprocess.Popen(command2)
                    # break

                if c == r:
                    print(c)
                    # set path of a file resize code here
                    print("On Pi-1 resize token received:: going to call resize task")
                    command = ["python3", "/home/pi-cv-101/pipeline-2/image-resizese-sendFog.py"]
                    subprocess.Popen(command)

                    # Run the QoE Alo to place next task

                    command2 = ["python3", "/home/pi-cv-101/pipeline-2/extract_imageobj_QoE.py"]
                    subprocess.Popen(command2)
                    break
                


        except FileNotFoundError:
            print("File not found. Make sure the file exists.")
        # if c== l:
        #     print(c)
        #     print("Got you")
        #     command = ["python3", "/home/administrator/Contribution-3/Automate_pipeline/testaftertokenreceived/filereceiver.py"]
        #     subprocess.Popen(command)   
        #     break
        # Wait for a short duration before reading the file again
    
        time.sleep(1)  # Adjust the sleep duration as needed


# Replace 'file.txt' with the path to your file
# Place the token file path here
while True:
	read_file_forever('/home/pi-cv-101/Compression_token.txt')

# if m == 5:
#     command = ["python3", "/home/administrator/Contribution-3/Automate_pipeline/testaftertokenreceived/filereceiver.py"]
#     subprocess.Popen(command)   
