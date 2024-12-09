# Execute the files with in the system only
import time
import subprocess

def read_file_forever(file_path):
    while True:
        try:
           
            l = "extract"
            # r = "resize"
            with open(file_path, 'r') as file:
                # Read the file contents here
                content = file.read()
                c = content.strip("\n")
                file.close()  #added
                f = open(file_path, 'w')
                f.write("Done")
                f.close()  #added
                if c == l:
                    print(c)
                    print("Got you")
                    

                    # time.sleep(2)
                    # set path of a file compression code here 
                    command = ["python3", "filesreceiver.py"]
                    subprocess.Popen(command)

                    # command2 = ["python3", "/home/administrator/Contribution-3/Automate_pipeline/testaftertokenreceived/compress_image_QoE.py"]
                    # subprocess.Popen(command2)
                    # break

                # if c == r:
                #     print(c)
                #     # set path of a file resize code here 
                #     command = ["python3", "/home/administrator/Contribution-3/Automate_pipeline/testaftertokenreceived/sleep.py"]
                #     subprocess.Popen(command)

                #     # Run the QoE Alo to place next task

                #     command2 = ["python3", "/home/administrator/Contribution-3/Automate_pipeline/testaftertokenreceived/compress_image_QoE.py"]
                #     subprocess.Popen(command2)
                #     break
                


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
read_file_forever('/home/angel/srinivas/Compression_token.txt')

# if m == 5:
#     command = ["python3", "/home/administrator/Contribution-3/Automate_pipeline/testaftertokenreceived/filereceiver.py"]
#     subprocess.Popen(command)   
