#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="A python script to list connected devices to a network")
    parser.add_argument("target-ip", help="target ip/ip range to perform the scan")
    return parser.parse_args()
  
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    device_list=[]    
    for i in ans:
        device_dict ={"ip": i[1].psrc, "mac": i[1].hwsrc }
        device_list.append(device_dict)
    
    return device_list


def print_result(device_list):
    print("IP\t\t\tMAC\n"+"-"*42)
    for i in device_list:
        print(i["ip"]+"\t\t"+i["mac"])


target = get_arguments()
print_result(scan(target))

