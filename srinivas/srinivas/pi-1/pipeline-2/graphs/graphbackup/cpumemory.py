import psutil
import matplotlib.pyplot as plt
from datetime import datetime
import time

def plot_cpu_memory_graph(interval_sec):
    timestamps = []
    cpu_percentages = []
    memory_percentages = []

    end_time = time.time() + interval_sec
    while time.time() < end_time:
        # Get CPU and memory usage
        cpu_percentage = psutil.cpu_percent()
        memory_percentage = psutil.virtual_memory().percent

        # Record timestamp and usage values
        timestamps.append(datetime.now())
        cpu_percentages.append(cpu_percentage)
        memory_percentages.append(memory_percentage)
        #cpu_percentages.append(cpu_percentage)

        # Wait for a short interval
        time.sleep(1)

    # Plot CPU usage
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot( cpu_percentages, marker='o')
    plt.title('CPU Usage Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('CPU Percentage')
    plt.title(f'CPU Utilization\nMax: {max(cpu_percentages):.2f}% | Avg: {sum(cpu_percentages) / len(cpu_percentages):.2f}%')

    # Plot memory usage
    plt.subplot(2, 1, 2)
    plt.plot( memory_percentages, marker='o', color='r')
    plt.title('Memory Usage Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Memory Percentage')
    memory_max = max(memory_percentages)
    memory_avg = sum(memory_percentages) / len(memory_percentages)
    plt.title(f'Memory Utilization\nMax: {memory_max:.2f}% | Avg: {memory_avg:.2f}%')
    #plt.title(f'Memory Utilization\nMax: {memory_percentages:.2f}% | Avg: {memory_percentages:.2f}%')

    #plt.tight_layout()
    #plt.show()
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    output_file_path =  '/home/srinivas/Contribution-3/graphs/' 
    plt.savefig(output_file_path + str(current_datetime) + '.png')
    print(f"Graph saved to: {output_file_path}")

# Call the function with a 20-second interval
plot_cpu_memory_graph(4)
