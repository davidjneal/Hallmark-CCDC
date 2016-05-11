#!/usr/bin/python
# this script will open ports, then you're expected to perform an implicit deny

import subprocess, os, sys

# iptables -I INPUT -p tcp --dport 25 -j ACCEPT
# iptables -I INPUT -p udp --dport 25 -j ACCEPT

uid = os.getuid()

if uid != 0:
    print "Needs to be run by root, or use sudo"
    sys.exit(1)

print "Enter ports you want open and type exit when done."
print "Both TCP & UDP will be opened."
print

while True:
    try:
        port = raw_input('Port? : ')
    except SyntaxError:
        print "Thats not a port!"
        continue
    if port == "exit":
        print
        print "exiting"
        print
        exit()
    port = str(port)
    iptables_tcp = "iptables -I INPUT -p tcp --dport %s -j ACCEPT" % (port)
    iptables_udp = "iptables -I INPUT -p udp --dport %s -j ACCEPT" % (port)
    tcp_process = subprocess.Popen(iptables_tcp.split(), stdout=subprocess.PIPE)
    print tcp_process.communicate()[0]
    udp_process = subprocess.Popen(iptables_udp.split(), stdout=subprocess.PIPE)
    print udp_process.communicate()[0]
