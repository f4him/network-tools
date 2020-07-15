#!/usr/bin/env python

import subprocess
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="A python script to change mac address of network interfaces")
    parser.add_argument("interface", help="Interface name to change MAC address")
    parser.add_argument("mac", help="New MAC address")
    options = parser.parse_args()
    return options



def change_mac(interface, new_mac):
    print("[+] Changing mac address for "+interface+" to "+new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig" , interface , "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
