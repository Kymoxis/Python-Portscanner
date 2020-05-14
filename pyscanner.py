#!/bin/python3
# Title.........:  Python-Portscanner
# Description...:  A simple colorful Python TCP Port Scanner; just for a quick scan.
# Author........:  MxMarl
# Version.......:  1.0
# Usage.........:  python3 pyscanner.py <ip> <starting Port> <End Port>
# Python Version:  3 

# TODO:
# List with known Ports
# Network Scan for alive Hosts


import sys
import socket
import time

try:
    from colorama import init
    init()

except ModuleNotFoundError:
    print("[FAIL] You Need to install the colorama modul!\nUsage: pip install colorama")
    sys.exit()


class StrCoL:
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    
    
# Some vars
col_fail = StrCoL.BOLD + StrCoL.FAIL + "[FAIL] " + StrCoL.ENDC
col_info = StrCoL.BOLD + StrCoL.YELLOW + "[INFO] "
col_smile = StrCoL.YELLOW + " :)" + StrCoL.ENDC
syntax_info = "Syntax: python pyscanner.py <ip> <starting Port> <End Port>"
example_info = "Example: python pyscanner.py 192.168.2.1 1 1023"

try:
    if sys.argv[1].lower() == "--help":
        print("PyScanner is a simple colorful Python TCP Port Scanner; just for a quick scan.")
        print(syntax_info)
        print(example_info)
        sys.exit()

    # Target definition
    if len(sys.argv) == 4:
        target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
        stp = int(sys.argv[2])  # Starting Port
        enp = int(sys.argv[3])  # End Port
        if stp > enp and not stp > 65535 and not stp < 0 and not enp < 0:
            print(col_fail + "Start Port can't be higher than End Port!")
            sys.exit()
        elif stp == enp and stp > 0 and enp > 0:
            print(col_fail + StrCoL.ENDC + "Start Port and End Port can't be the same!")
            sys.exit()
        elif stp < 0 or enp < 0:
            print(col_fail + "Ports can't go deeper than 0!" + col_smile)
            sys.exit()
        elif stp > 65535 or enp > 65535:
            print(col_fail + "Ports can't be higher than 65535!")
            sys.exit()

    print(StrCoL.BOLD + StrCoL.YELLOW + "-" * 50 + StrCoL.ENDC)
    print("Scanning target " + target + " | TCP Port {}".format(stp) + "-{}".format(enp))
    print(StrCoL.BOLD + StrCoL.YELLOW + "-" * 50 + StrCoL.ENDC)


except (IndexError, ValueError, NameError):
    print(col_fail + "Invalid argument!\n%s" % syntax_info + StrCoL.ENDC)
    print(example_info)
    sys.exit()

except socket.gaierror:
    print(col_fail + StrCoL.ENDC + "Hostname couldn't be resolved\n%s" % syntax_info + StrCoL.ENDC)
    sys.exit()

try:
    count = 0
    start_time = time.time()
    for port in range(stp, enp):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.01)
        result = s.connect_ex((target, port))  # Return error indicator
        if result == 0:
            print("%s" % target + StrCoL.BOLD + StrCoL.BLUE + ":{}".format(port) + StrCoL.ENDC + " /TCP is open")
            count += 1
        s.close()
    elapsed_time = time.time() - start_time
    print("\n" + col_info + StrCoL.ENDC + "TCP scan for %s completed\nFound: %d Open TCP Ports" % (target, count))
    print("Duration: %s [min|sec]\n" % time.strftime("%M:%S", time.gmtime(elapsed_time)))

except KeyboardInterrupt:
    print(col_info + StrCoL.ENDC + "Exiting program...")
    sys.exit()

except socket.error:
    print(col_fail + StrCoL.ENDC + "Couldn't connect to server.")
    sys.exit()
