import psutil
import matplotlib.pyplot as plt
import time

# Define the time interval for data collection (in seconds) and the number of data points to display
time_interval = 1
num_data_points = 60

# Initialize empty lists to store CPU and memory utilization data
cpu_data = []
memory_data = []

# Create a function to update the data
def update_data():
    cpu_percent = psutil.cpu_percent(interval=None)
    virtual_memory = psutil.virtual_memory()
    cpu_data.append(cpu_percent)
    memory_data.append(virtual_memory.percent)

# Create a function to update the graph
def update_graph():
    plt.clf()  # Clear the previous graph
    plt.subplot(1, 2, 1)  # First subplot for CPU
    plt.plot(cpu_data, label='CPU %')
    plt.xlabel('Time (s)')
    plt.ylabel('CPU %')
    plt.title('CPU Utilization')
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)  # Second subplot for Memory
    plt.plot(memory_data, label='Memory %')
    plt.xlabel('Time (s)')
    plt.ylabel('Memory %')
    plt.title('Memory Utilization')
    plt.grid(True)
    plt.legend()

# Create a figure and subplots
plt.figure(figsize=(10, 6))
plt.ion()  # Turn on interactive mode for live plotting

# Start data collection and graph update
for _ in range(num_data_points):
    update_data()
    update_graph()
    plt.pause(time_interval)

# Keep the graph window open after the script completes
plt.ioff()
plt.show()
