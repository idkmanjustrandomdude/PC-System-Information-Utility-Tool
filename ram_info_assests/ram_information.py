import psutil
ram = psutil.virtual_memory()
total_ram = ram.total
total_ram_in_gb = total_ram / 1073741824
ram_used = ram.used
ram_free = ram.free
ram_used_in_gb = ram_used / 1073741824
ram_free_in_gb = ram_free / 1073741824
ram_used_percentage = (ram_used_in_gb / total_ram_in_gb) * 100
ram_free_percentage = (ram_free_in_gb / total_ram_in_gb) * 100

def ram_info (): 
    print("in what units do you want to see ram info in?")
    print("[1] Gigabyte (GB) ")
    print("[2] bytes")
    units_choice = int(input("Type in the number: "))
    if units_choice == 1:
        print("====================================================")
        print("")
        print("                  RAM INFORMATION                   ")
        print("")
        print("====================================================")
        print(f"RAM total: {total_ram_in_gb} GB")
        print(f"RAM used: {ram_used_in_gb} GB")
        print(f"RAM free: {ram_free_in_gb} GB")

    if units_choice == 2:
        print("====================================================")
        print("")
        print("                  RAM INFORMATION                   ")
        print("")
        print("====================================================")
        print(f"RAM total: {total_ram} bytes")
        print(f"RAM used: {ram_used} bytes")
        print(f"RAM free: {ram_free} bytes")
        print(" ")
    ram_percentage_choice = input("do you like to see current ram usage in precntage? (y/n)")
    if ram_percentage_choice == "y":
        print("====================================================")
        print("")
        print("                   RAM PERCENTAGE                   ")
        print("")
        print("====================================================")
        print(f"Current usage RAM percentage: {ram_used_percentage}%")
        print(f"Current usable RAM percentage: {ram_free_percentage}%")

    if ram_percentage_choice == "n":
        print(" ")

    print("===========================================================")
    print("")
    print("What action do you wanna do next?")
    print("[1] Go back")
    print("[2] Exit")
    print("[3]  Refresh")
    print("")
    print("===========================================================")
    options_choice = int(input("pls write the number from (1-3): "))
    import sys
    if options_choice == 1:
        return
    if options_choice == 2:
        sys.exit()
    if options_choice == 3:
        ram_info()

ram_info