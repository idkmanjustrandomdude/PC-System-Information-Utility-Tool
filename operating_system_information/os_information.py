import platform
def os_info():
    os_system = platform.system()
    os_system_type = platform.release()
    os_version = platform.version()
    print(f"The installed OS type is: {os_system} ")
    print(f"The installed OS version is: {os_system_type}")
    print(f"The installed OS sub-verison is: {os_version}")
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
        os_info()


os_info
