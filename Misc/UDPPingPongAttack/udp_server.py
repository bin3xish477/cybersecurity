#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep

IP = "0.0.0.0"
PORT = 1234

def start_server():
	sock = socket(AF_INET, SOCK_DGRAM)
	# no use of listen or accept() in udp servers
	# b/c udp is connectionless
	sock.bind((IP, PORT))

	while True:
		data, (ip, port) = sock.recvfrom(1024)
		data = data.decode("utf-8")
		print(f"From {ip}:{port} :")
		print(f"Message: {data}")
		sleep(1)
		sock.sendto(b'Thank you for the message', (ip, PORT))

if __name__ == '__main__':
	start_server()