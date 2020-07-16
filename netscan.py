#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    

    device_list=[]


    print("IP\t\t\tMAC\n-----------------------------------------")
    
    for i in ans:
        device_dict ={"ip": i[1].psrc, "mac": i[1].hwsrc }
        device_list.append(device_dict)
    

    return device_list


def print_result(device_list):
    print("IP\t\t\tMAC\n------------------------------------")
    for i in device_list:
        print(i["ip"]+"\t\t"+i["mac"])



print_result(scan('192.168.0.1/24'))