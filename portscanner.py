
import socket
import termcolor

def scan(target, ports):
    for port in range(1,ports):
        scan_port(target,port)
        
        
def scan_port(ipaddress, port)    # This port will try to connect with the ip address and port specified and print what ports are open. You can print closed port stuff but I have preferred to use pass as that output won't be important for us.
    try:
        sock = socket.socket()
        sock.connect((ipaddress,port))
        print("[+] Port Opened "+ str(port))
   except:
          pass
    
targets = input("[*] Enter targets to scan (split them by having a comma ,)")
ports = int(input("[*] Enter How many ports you wish to scan"))                                 # This would be the last number like if you wish to first 100 ports, it will scan 1- 100 ports.

if ',' in targets:
                print("[*] Scanning Multiple Targets")
                for ip_addr in targets.split(','):
                                                scan(ip_addr.strip(' '),ports)
                    
else:
    scan(targets,ports)
