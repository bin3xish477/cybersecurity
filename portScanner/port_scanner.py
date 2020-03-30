#!/usr/bin/env python3

try:
    import socket
    from sys import exit, argv
    from os import _exit
except ImportError as err:
    print("Import error: {err}")

def portScan(target_ip, start, finish):
    print(f'Scanning ports on target: \033[32m\033[01m{target_ip}\033[0m')
    print(f'Port range: \033[95m\033[01m{start}-{finish}\033[0m\n')
    for i in range(start, finish + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            try:
                soc.settimeout(3)
                soc.connect((target_ip, i))
                print(f'\033[31m\033[01m{i}\033[0m::\033[37mopen\033[0m')
                try:
                    data = soc.recv(1024).decode(errors='ignore')
                    if not data:
                        continue
                    print(data)
                except socket.error:
                    continue
            except ConnectionRefusedError:
                continue
            finally:
                soc.close()

def main():
    if len(argv) != 4:
        print('\033[31m', 'Usage: ./port_scanner.py TARGET_IP START_PORT FINISH_PORT', '\033[0m')
        exit(1)
    TARGET, START, FINISH = argv[1], int(argv[2]), int(argv[3])
    portScan(TARGET, START, FINISH)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            print('\033[31m', 'Exiting scanner...', '\033[0m')
            exit(1)
        except SystemExit:
            _exit(1)
