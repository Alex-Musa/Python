from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()  # CREATE EMPTY LIST FOR HOLDING DEVICES

# FOR LOOP TO CREATE LARGE NUMBER OF DEVICES
for index in range(1, 10):
    # CREATE DEVICE DICTIONARY
    device = dict()

    # RANDOM DEVICE NAME
    device["name"] = (
            choice(["R2", "R3", "R4", "R6", "R10"])
            + choice(["L", "U"])
            + choice(string.ascii_letters)
    )

    # RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER, Aruba
    device["vendor"] = choice(["Cisco", "Juniper", "Aruba"])
    if device["vendor"] == "Cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010," "20.1"])

    elif device["vendor"] == "Juniper":
        device["os"] = "junos"
        device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010," "20.1"])

    elif device["vendor"] == "Aruba":
        device["os"] = "ArubaOS"
        device["version"] = choice(["8.8.x", "8.7.x", "8.12.x" "8.6.x"])

    device["ip"] = "10.1.1." + str(index)

    # NICELY FORMATTED PRINT OF THIS ONE DEVICE
    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")

    # ADD THIS DEVICE TO THE LIST OF DEVICES
    devices.append(device)

# USE PPRINT TO PRINT DATA AS-IS
print("\n ----- DEVICES AS LIST OF DICTS -------")
pprint(devices)

# USE 'tabulate' TO PRINT TABLE OF DEVICES
print("\n ----- DEVICES AS LIST OF DICTS -------")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))

