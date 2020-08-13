#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_DGRAM

IP = "0.0.0.0"
PORT = 1234

def start_server():
	sock = socket(AF_INET, SOCK_DGRAM)
	# no use of listen or accept() in udp servers
	sock.bind((IP, PORT))

	while True:
		data, (ip, port) = sock.recvfrom(1024)
		print(f"From {ip}:{port} :")
		print(f"Message: {data}")

		sock.sendto(b'Thank you for the message', (ip, PORT))

if __name__ == '__main__':
	start_server()