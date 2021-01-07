from socket import socket
from subprocess import run, PIPE

pattern_size=100

msf_pattern=run(
    ['msf-pattern_create', '-l', str(pattern_size)], 
    stdout=PIPE, stderr=PIPE
)

msf_pattern=str(msf_pattern.stdout)[2:-1].rstrip("\\n")

print(msf_pattern)
