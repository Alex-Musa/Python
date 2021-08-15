from pprint import pprint

# Dictionary repersenting a device
device = {
    "name": "sbx=n9kv-ao",
    "vendor": "Cisco",
    "model": "Nexus900 C9300V Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
}

# SIMPLE PRINT
print("\n ________ SIMPLE PRINT ________")
print("device", device)
print("device name", device["name"])

# PRENT PRINT
print("\n_____ PRENT PRINT _____")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT
print("\n _____ FOR LOOP, USING F-STRING ___________________")
for key, value in device.items():
    print(f"{key:>16s} : {value}")
