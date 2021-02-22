from socket import socket
from string import ascii_letters, digits

conn = ("challenges.ctfd.io", 30468)

flag = "flag{"

chars = f"{ascii_letters}{digits}"

while not flag.endswith("}"):
    for letter in chars:
        temp_flag = f"{flag}{letter}"
        print(temp_flag)
        with socket() as soc:
            soc.connect(conn)
            soc.send(bytes(temp_flag, "utf8"))
            resp = soc.recv(1048)
            if b"You seem" in resp:
                flag += letter
                print(flag)


