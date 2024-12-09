import psutil
import matplotlib.pyplot as plt
import os  # Import the os module for file path operations
import time

# Define the time interval for data collection (in seconds) and the number of data points to collect
time_interval = 1
num_data_points = 10

# Initialize empty lists to store CPU and memory utilization data
cpu_data = []
memory_data = []

# Create a function to collect data
def collect_data():
    for _ in range(num_data_points):
        cpu_percent = psutil.cpu_percent(interval=None)
        virtual_memory = psutil.virtual_memory()
        cpu_data.append(cpu_percent)
        memory_data.append(virtual_memory.percent)
        time.sleep(time_interval)

# Collect data
collect_data()

# Create a function to plot the graphs
def plot_graphs():
    plt.figure(figsize=(12, 6))  # Set the figure size for side-by-side graphs
    
    # Subplot for CPU
    plt.subplot(1, 2, 1)  # Create a 1x2 grid for two subplots, select the first one
    plt.plot(cpu_data, label='CPU %')
    plt.xlabel('Time (s)')
    plt.ylabel('CPU %')
    plt.title(f'CPU Utilization\nMax: {max(cpu_data):.2f}% | Avg: {sum(cpu_data) / len(cpu_data):.2f}%')
    plt.grid(True)
    plt.legend()

    # Subplot for Memory
    plt.subplot(1, 2, 2)  # Select the second subplot
    plt.plot(memory_data, label='Memory %')
    plt.xlabel('Time (s)')
    plt.ylabel('Memory %')
    memory_max = max(memory_data)
    memory_avg = sum(memory_data) / len(memory_data)
    plt.title(f'Memory Utilization\nMax: {memory_max:.2f}% | Avg: {memory_avg:.2f}%')
    plt.grid(True)
    plt.legend()

    # Save the figure to /tmp directory
    output_file_path = '/home/srinivas/Contribution-3/graphs/utilization_graph.png'
    plt.savefig(output_file_path)
    print(f"Graph saved to: {output_file_path}")

# Plot the graphs
plot_graphs()
