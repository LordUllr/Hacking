#Script NMap Automation

import nmap

scanner = nmap.PortScanner()

spacer = "-" * 50
apr = "Hello, I'm a simple port scanner with Nmap Tool"

#Apresentation
print(spacer)
print(apr.center(50))
print(spacer)

#Functions


def n_scan(host, prot_type, type): #Scan the IP
    scanner.scan(host, '1-1024', prot_type[type][1])
    if scanner[host].state() == 'up':
        print(f"Scanner Status: \033[1;32m{scanner[host].state()}\033[0;0m")
        print(spacer)
        print(f"Host: \033[1;32m{host} ({scanner[host].hostname()})\033[0;0m")
        for proto in scanner[host].all_protocols():
            print(spacer)
            print(f"Protocol : \033[1;32m{proto}\033[0;0m")
            lport = scanner[host][proto].keys()
            for port in lport:
                print(f"port : \033[1;32m{port} \033[0;0m\tstate : \033[1;32m{scanner[host][proto][port]['state']}\033[0;0m")
    else:
        print(f"The IP \033[1;32m{host}\033[0;0m is \033[1;31mDown\033[0;0m!")


def select_type(): #Select the type of scan
    type = int(input("\033[1;30m\033[1;102mSelect the type of scan you want to run:\n\033[0;0m"
                     "1. SYN ACK Scan\n"
                     "2. UDP Scan\n"
                     "3. Comprehensive Scan\n"))
    prot_type = {1: ["SYN ACK Scan", "-v -sS"], 2: ["UDP Scan", "-v -sU"],
              3: ["Comprehensive Scan", "-v -sS -sV -sC -A -O"]}
    if type not in prot_type.keys():
        print("\033[1;91mPlease, insert a valid option!\033[0;0m")
        return select_type()
    else:
        print(f"You have select \033[1;30m{prot_type[type][0]}\033[0;0m\n\033[1;33mStarting Scan!\033[0;0m")
        n_scan(host, prot_type, type)


def add_host(): #add the ip of host to scan
    global host
    host = str(input("\033[1;30m\033[1;102mPlease, enter the IP adrress you want to scan:\n\033[0;0m"))
    print(f"The IP is: \033[1;92m{host}\033[0;0m")
    confirm = input("Correct?\n\033[1;92m(Y)Yes\033[0;0m / \033[1;91m(N)No\033[0;0m\n")
    while confirm not in "yY":
        return add_host()
    else:
        select_type()
        return host


add_host()
