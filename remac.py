#!/usr/bin/env python3

import subprocess
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="A python script to change mac address of network interfaces",
    epilog="Note: Check the output of 'ifconfig' or 'netstat -i' to see list of available network interfaces. Also keep in mind that rebooting will restore the default mac address.")
    parser.add_argument("interface", help="Interface name to change MAC address")
    parser.add_argument("mac", help="New MAC address")
    return parser.parse_args()



def change_mac(interface, new_mac):
    print("[+] Changing mac address for "+interface+" to "+new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig" , interface , "up"])

options = get_arguments()
change_mac(options.interface, options.mac)
