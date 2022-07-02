#Script NMap Automation

import os
import sys
from art import *
from termcolor import colored

ans = True
separator = "=" * 100


def menu():
    global ans

    clear()

    while ans:
        print(separator)
        print(colored(text2art("NMap Automation"), "cyan"))
        print(colored("Created By: LordUllr", "magenta"))
        print(colored("Version: 1.0", "red"))
        print(separator)

        print(
            colored("\n1. Scan An IP Address For Open Ports using TCP",
                         "yellow",
                         attrs=["bold"]))
        print(
            colored("2. Scan An IP Address For Open Ports using UDP",
                         "yellow",
                         attrs=["bold"]))
        print(colored("3. Operating System Scan", "yellow", attrs=["bold"]))
        print(
            colored("4. Agressive Scan For An IP Address",
                         "yellow",
                         attrs=["bold"]))
        print(
            colored("5. Scan The Network For All Devices",
                         "yellow",
                         attrs=["bold"]))
        print(
            colored("6. Exit\n", "yellow", attrs=["bold"])
        )
        print(colored("-" * 48, "green"))
        opt = input(colored("What would you like to do? Enter your selection: ", "green")).upper()

        if opt == "1":
            tcp_scan()
        if opt == "2":
            udp_scan()
        if opt == "3":
            os_scan()
        if opt == "4":
            a_scan()
        if opt == "5":
            net_scan()
        if opt == "6":
            print(colored(text2art("\nBye!", "small"), "red"))
            ans = False
        else:
            n_valid(menu, int(opt))


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def n_valid(func, var):
    if var > 6:
        clear()

        print(
            colored("\nNot Valid Choice Try Again\n",
                    "red",
                    attrs=["reverse"]))
        func()


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def dir_output(var, path, url):
    if len(var) == 0:
        var = path + "/" + url
        return var


def tcp_scan():
    global ans
    clear()

    print(colored("=" * 52, "cyan"))
    print(colored(text2art("TCP SCAN"), "cyan"))
    print(colored("=" * 52, "cyan"))
    tcp_host = input(
        colored("Enter the IP you want scan: ", "green")
    )
    exp = input(colored("\nWant export result to file?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if exp in "yY":
        tcp_output = str(input(colored(f"Enter the output folder - [default: reports/Nmap/{tcp_host}/]: ",
                "green",
            )))
        tcp_output = dir_output(tcp_output, "reports/Nmap/", tcp_host)
        create_dir(tcp_output)
        os.system(f"sudo nmap -sS {tcp_host} -o {tcp_output}/tcpscan.txt")
        print(colored("File exported", "green"))
    else:
        os.system(f"sudo nmap -v -sS {tcp_host}")
    opt = input(colored("\nReturn to main menu?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if opt in "yY":
        clear()
        menu()
    else:
        print(colored(text2art("\nBye!", "small"), "red"))
        ans = False


def udp_scan():
    global ans
    clear()

    print(colored("=" * 52, "green"))
    print(colored(text2art("UDP SCAN"), "green"))
    print(colored("=" * 52, "green"))
    udp_host = input(
        colored("Enter the IP you want scan: ", "green")
    )
    exp = input(colored("\nWant export result to file?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if exp in "yY":
        udp_output = str(input(colored(f"Enter the output folder - [default: reports/Nmap/{udp_host}/]: ",
                "green",
            )))
        udp_output = dir_output(udp_output, "reports/Nmap/", udp_host)
        create_dir(udp_output)
        os.system(f"sudo nmap -sU {udp_host} -o {udp_output}/udpscan.txt")
        print(colored("File exported", "green"))
    else:
        os.system(f"sudo nmap -v -sU {udp_host}")
    opt = input(colored("\nReturn to main menu?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if opt in "yY":
        clear()
        menu()
    else:
        print(colored(text2art("\nBye!", "small"), "red"))
        ans = False


def os_scan():
    global ans
    clear()

    print(colored("=" * 52, "yellow"))
    print(colored(text2art("OS SCAN"), "yellow"))
    print(colored("=" * 52, "yellow"))
    os_host = input(
        colored("Enter the IP you want scan: ", "green")
    )
    exp = input(colored("\nWant export result to file?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if exp in "yY":
        os_output = str(input(colored(f"Enter the output folder - [default: reports/Nmap/{os_host}/]: ",
                "green",
            )))
        os_output = dir_output(os_output, "reports/Nmap/", os_host)
        create_dir(os_output)
        os.system(f"sudo nmap -O {os_host} -o {os_output}/osscan.txt")
        print(colored("File exported", "green"))
    else:
        os.system(f"sudo nmap -O {os_host}")
    opt = input(colored("\nReturn to main menu?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if opt in "yY":
        clear()
        menu()
    else:
        print(colored(text2art("\nBye!", "small"), "red"))
        ans = False


def a_scan():
    global ans
    clear()

    print(colored("=" * 96, "red"))
    print(colored(text2art("AGRESSIVE SCAN"), "red"))
    print(colored("=" * 96, "red"))
    a_host = input(
        colored("Enter the IP you want scan: ", "green")
    )
    exp = input(colored("\nWant export result to file?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if exp in "yY":
        a_output = str(input(colored(f"Enter the output folder - [default: reports/Nmap/{a_host}/]: ",
                "green",
            )))
        a_output = dir_output(a_output, "reports/Nmap/", a_host)
        create_dir(a_output)
        os.system(f"sudo nmap -T4 -A {a_host} -o {a_output}/ascan.txt")
        print(colored("File exported", "green"))
    else:
        os.system(f"sudo nmap -T4 -A {a_host}")
    opt = input(colored("\nReturn to main menu?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if opt in "yY":
        clear()
        menu()
    else:
        print(colored(text2art("\nBye!", "small"), "red"))
        ans = False


def net_scan():
    global ans
    clear()

    print(colored("=" * 96, "red"))
    print(colored(text2art("AGRESSIVE SCAN"), "red"))
    print(colored("=" * 96, "red"))
    net_host = input(
        colored("Enter your address and range (i.e. 192.168.0.1/24) now: ", "green")
    )
    net_sort = net_host.split("/", 1)
    net_sort = net_sort[0]
    exp = input(colored("\nWant export result to file?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if exp in "yY":
        net_output = str(input(colored(f"Enter the output folder - [default: reports/Nmap/{net_sort}/]: ",
                "green",
            )))
        net_output = dir_output(net_output, "reports/Nmap/", net_sort)
        create_dir(net_output)
        os.system(f"sudo nmap -sn {net_host} -o {net_output}/netscan.txt")
        print(colored("File exported", "green"))
    else:
        os.system(f"sudo nmap -sn {net_host}")
    opt = input(colored("\nReturn to main menu?\n Y - Yes\n N - No\n >>> ", "green")).upper()
    if opt in "yY":
        clear()
        menu()
    else:
        print(colored(text2art("\nBye!", "small"), "red"))
        ans = False


try:
    menu()

except KeyboardInterrupt:
    print("\n \n Keyboard Interrupt. ")
    sys.exit()
