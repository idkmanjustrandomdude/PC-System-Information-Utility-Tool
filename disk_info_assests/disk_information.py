import psutil


def disk_info():
    for partition in psutil.disk_partitions():
        disk_drive = partition.device
        disk_mountpoint = partition.mountpoint
        disk_type = partition.fstype
        disk_usage = psutil.disk_usage(disk_mountpoint) 


        print("=================================================")
        print("                DISK INFORMATION                 ")
        print("=================================================")
        print("")
        print(f"The current disk are: {disk_drive}")
        print(f"The disk mount point is: {disk_mountpoint}")
        print(f"the disk mount type is: {disk_type} ")
        print(f"The current disk uasge is: ")
        print(f"Total space : {disk_usage.total / (1024**3):.2f} GB")
        print(f"Used space  : {disk_usage.used / (1024**3):.2f} GB")
        print(f"Free space  : {disk_usage.free / (1024**3):.2f} GB")
        print(f"Usage       : {disk_usage.percent}%")
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
        disk_info()


if __name__ == "__main__":
    disk_info()   