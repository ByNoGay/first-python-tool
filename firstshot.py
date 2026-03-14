
import sys
from scapy.all import sr1, IP, ICMP

p = sr1(IP(dst=sys.argv[1])/ICMP(), timeout = 2)

if(p == None):
    print("no answer...")
else:
    p.show
