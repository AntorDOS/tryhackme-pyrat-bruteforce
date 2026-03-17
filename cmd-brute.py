#!/bin/python3

import socket

host ="10.49.163.39"
port = 8000
wordlists = "/usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt"


def cmd(wordlists):
    try:
        with open(wordlists, 'r') as file:
            for line in file:
                cmd = line.strip()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                s.sendall(cmd.encode() + b'\n')
                response = s.recv(1024).decode().strip()
                if response != "" and "is not defined" not in response and "leading zeros" not in response:
                    print(f"[+] valied cmd found: {cmd}")
                    print(f"The response of {cmd} is: {response}")
                    

    except KeyboardInterrupt:
        exit()
    except FileNotFoundError:
        print("Put The Right File Path")
cmd(wordlists)
