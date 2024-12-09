import psutil
import re
# def get_max_cpu_speeds():
#     try:
#         # Get information about the CPU
#         cpu_info = psutil.cpu_info()

#         # Extract the max CPU speed
#         max_cpu_speed = max(info.current for info in cpu_info)

#         return max_cpu_speed
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# if __name__ == "__main__":
#     max_speed = get_max_cpu_speeds()
#     if max_speed is not None:
#         print(f"Maximum CPU Speed: {max_speed} MHz")
cpuspeed = psutil.cpu_freq()
# print(cpuspeed)
maxcpu= str(cpuspeed)

max_value = re.search(r"max=(\d+)", maxcpu)

if max_value:
    max_cpu_speed = max_value.group(1)
    print(max_cpu_speed)
else:
    print("Max value not found.")
# max_cpu_speed = max(info.current for info in cpu_info)
# print(max_cpu_speed)