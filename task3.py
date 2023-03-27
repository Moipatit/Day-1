#!/usr/bin/env python
from scapy.all import *
def print_summary(pkt):
    if IP in pkt:
        ip_src=pkt[IP].src
        ip_dst=pkt[IP].dst
        print(" IP source " + str(ip_src))
        print(" IP destination " + str(ip_dst))

        
sniff(filter="ip", prn=print_summary, store=0)