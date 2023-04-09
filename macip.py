#!/usr/bin/python3

# quick script to discover the local raspberry pi machines since their IP's change using DHCP
# the arp-scan command is used.
# administrator password will be required.

import os
import sqlite3
from datetime import datetime, timedelta
import machine

logtime = datetime.now() + timedelta(hours=7)

data = os.popen('sudo arp-scan --localnet -I en0')
data = data.read().split('\n')

machine_list = machine.machine_list

# list of all known maching MAC addresses.
# this was found using "sudo arp-scan -l -I en0" on the mac
known_machines = {
  'PI 400': 'e4:5f:01:07:5c:67',
  'Desktop Pi (office)': 'dc:a6:32:b3:38:a6',
  'Touchscreen Pi': 'dc:a6:32:cb:dc:ae',
  'Epson Printer': '00:26:ab:bc:61:e8'
}

def isKnown(mac):
  if mac in known_machines.values():
    return True

  return False

def getKnown(mac):
  for key, value in known_machines.items():
    if value == mac:
      return key

  return 'UNKNOWN'

for machine in data:
  if '192.168.1' in machine:
    arr = machine.split()
    # this line will print all found machines on the local network.
    # print(f'found: {arr[0]} = {arr[1]} >> {arr[2:]}')
    if isKnown(arr[1]):
      print(f'{arr[0]} = {arr[1]}', end = ' : ')
      print('{}'.format(getKnown(arr[1])))


