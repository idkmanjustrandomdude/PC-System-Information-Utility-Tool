import platform
import psutil
def cpu_info():

    cpu_name = platform.processor()
    cpu_architecture = platform.architecture()[0]
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)

    print("====================================================")
    print("")
    print("                  CPU INFORMATION                   ")
    print("")
    print("====================================================")
    print(f"CPU Name:  {cpu_name}")
    print(f"CPU Architecture: {cpu_architecture}")
    print(f"CPU Cores: {cpu_cores}")
    print(f"CPU Threads: {cpu_threads}")

cpu_info