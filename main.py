from cpu_info_assets.cpu_information import cpu_info
from ram_info_assests.ram_information import ram_info
from disk_info_assests.disk_information import disk_info
from operating_system_information.os_information import os_info

while True:

    print("---------------------------------------------------------")
    print("what do want to see? ")
    print("")
    print("========================================================")
    print("[1]                  CPU information                    ")
    print("[2]                  RAM information                    ")
    print("[3]                 Disk information                    ")
    print("[4]            operating system information             ")
    print("========================================================")
    print("")
    print("---------------------------------------------------------")
    info_choice = int(input("Enter your choice (1-4): "))
    print("")


    if info_choice == 1:
        print("please wait...")
        print("loading..")
        cpu_info()

    if info_choice == 2:
        print("please wait..")
        print("loading..")
        ram_info()

    if info_choice == 3:
        print("please wait..")
        print("loading..")
        disk_info()

    if info_choice == 4:
        print("please wait..")
        print("loading..")
        os_info()

    print("")

    for_exit = input("press enter to exit.")