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
    print("")
    print("===========================================================")
    print("")
    print("What action do you wanna do next?")
    print("[1] Go back")
    print("[2] Exit")
    print("[3]  Refresh")
    print("")
    print("===========================================================")
    print("")
    options_choice = int(input("pls write the number from (1-3): "))
    import sys
    if options_choice == 1:
        return
    if options_choice == 2:
        sys.exit()
    if options_choice == 3:
        cpu_info()

cpu_info