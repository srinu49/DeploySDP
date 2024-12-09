import psutil

def get_cpu_available_percentage():
    cpu_percentage = psutil.cpu_percent(interval=1, percpu=False)
    cpu_available_percentage = 100.0 - cpu_percentage
    return cpu_available_percentage
    
def get_memory_available_percentage():
    memory = psutil.virtual_memory()
    memory_available_percentage = 100.0 * memory.available / memory.total
    return memory_available_percentage

def available_resources(cpu_percent, memory_percent):
   weight = 0.5 
   resources = weight*cpu_percent + weight* memory_percent
   return resources


if __name__ == "__main__":
    cpu_available_percentage = get_cpu_available_percentage()
    #print(cpu_available_percentage)
    memory_available_percentage = get_memory_available_percentage()
    #print(f"Memory Available Percentage: {memory_available_percentage:.2f}%")
    resource_availability = available_resources(cpu_available_percentage, memory_available_percentage)
    print(resource_availability)
